from LibDatabase import LibDatabase

mydb = LibDatabase()

class Book:
  
    def __init__(self, userID):
        self.userID = userID

    # insert/enter book
    def insert_book(self):
        bookID = input('Enter Book ID: ')
        title = input('Enter Book Title: ')
        author = input('Enter Book author: ')
        language = input('Enter Book language: ')
        pub_year = input('Enter Book publication year: ')
        
        # save to the databse
        mydb.insert_book(self.userID, bookID, title, author, language, pub_year)
        print('Book added successfully')
        

    # update book
    def update_book(self):
    
        # get the info of the book you want to update
        BookID = input('Enter Book ID: ')

        # check for it in the database
        mydb.search_book(BookID)
        
        if not None:
            book_count = input('What is the Book Count?: ')
            # save to database
            mydb.update_book(BookID, book_count)
            print('Book updated successfully')
           
    
    # view book function
    def view_book(self):

        BookID = input('Enter Book ID: ')
        # check for it in the database
        book_details = mydb.search_book(BookID)

        if book_details != None:
            print(f"""
                    Title ------> {book_details[0]}
                    Number of Books Available -------> {book_details[1]}
                    Author(s) --------> {book_details[2]}
                """)
        else:
            print('Book does not exist!')
            

    # search by specific things
    def search_by_anything(self):
        """
        This function searches for book by
        Title, Author, Language or Publication Year
        """
        data = input('Search by Title or Author or Year or Language: ')

        # check dtabase
        feedback = mydb.search_by_anything(data)
        
        if feedback:
            for detail in feedback:
                print(f"""
                    'BookID'------> {detail[0]}
                    Title ------> {detail[1]}
                    Author(s) -------> {detail[2]}
                    Language --------> {detail[3]}
                    Year -----------> {detail[4]}
                """)
          
        else:
            print('Sorry, the Book does not exist')

        # show the number f returned books
        print(f' You have {len(feedback)} hits')

    
    # checkout or borrow books
    def borrow_book(self):
        
        # get book ID
        bookID = input('Enter the ID of the book you want to borrow: ')

        # # check in database 
        available = mydb.borrow_book(self.userID, bookID)

        if available == None:
            print(f'Book is currently not available!')
        elif available == False:
            print('You have already borrowed this book!')
        else:
            print('You have successfully borrowed this book')

    
     # return book
    def return_book(self):
        # get user ID
        bookID = input('Enter the ID of the book you want to return: ')

        # # check in database 
        return_book = mydb.return_book(self.userID, bookID)

        if return_book == None:
            print('You did not borrow this book')
        else:
            print('Book returned successfully')

    
    # reserve books
    def reserve_book(self):
        
        # get book ID
        bookID = input('Enter the ID of the book you want to reserve: ')

        # # check in database 
        available = mydb.reserve_book(self.userID, bookID)

        if available == None:
            print(f'Book is currently not available!')
        else:
            print('You have successfully reserved this book')

    
    # book history
    def book_history(self):
        
        # get book ID
        date = input('Enter the date : ')

        # # check in database 
        history = mydb.book_history(date)

        if history == None:
            print(f'There are no history available!')
        else:
            for detail in history:
                print(f"""
                    User ------> {detail[0]}
                    BookID -------> {detail[1]}
                    is_Added --------> {detail[2]}
                    is_Borrowed -----------> {detail[3]}
                    is_Returned -----------> {detail[4]}
                    Date -----------> {detail[5]}
                """)
            
