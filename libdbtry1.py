# from LibDatabase import LibDatabase
# # from LibMgtSys import LibMgtSys
# # write the CUD functionality for the book

# mydb = LibDatabase()
# # userID = LibMgtSys.login

# class Book:
#     # initialize class
#     # def __init__(self, title, author, language, publication):
#     #     self.title = title
#     #     self.author = author
#     #     self.language = language
#     #     self.publication = publication
#     def __init__(self):
#         # create an instance of the book
#         # self.book = Book()
#         pass
        
#         # self.cur = LibDatabase()

#     # insert/enter book
#     def insert_book(self):
#         # print('Insert Book')
#         #  title, author, language, and publication year
#         title = input('Enter Book Title: ')
#         author = input('Enter Book author: ')
#         language = input('Enter Book language: ')
#         pub_year = input('Enter Book publication year: ')
        
#         # save to the databse
#         mydb.insert_book(title, author, language, pub_year)
        

#     # update book
#     def update_book(self):
#         print('Update Book')
#         # get the info of the book you want to update
#         BookID = input('Enter Book ID: ')

#         # check for it in the database
#         mydb.search_book(BookID)
        

#         if not None:
#             book_count = input('What is the Book Count?: ')

#             # save to database
#             mydb.update_book(BookID, book_count)
           
    
#     # view book function
#     def view_book(self):
#         print('View Book')
#         # get the info of the book you want to update
#         BookID = input('Enter Book ID: ')

#         # check for it in the database
#         book_details = mydb.search_book(BookID)

#         if book_details != None:
#             print(book_details)

#     # search by specific things
#     def search_by_anything(self):
#         """
#         This function searches for book by
#         Title, Author, Language or Publication Year
#         """
#         data = input('Search by Title or Author or Year or Language: ')

#         # check dtabase
#         feedback = mydb.search_by_anything(data)
#         print(f'f {feedback}')
        
#         if feedback:
#             for detail in feedback:
#                 print(f"""
#                     'BookID'.....>
#                     Title ------> {detail[0]}
#                     Author(s) -------> {detail[1]}
#                     Language --------> {detail[2]}
#                     Year -----------> {detail[3]}
#                 """)
          
#         else:
#             print('Sorry, the Book does not exist')
        
#         print(f' You have {len(feedback)} hits')

    
#     # checkout or borrow books
#     def borrow_book(self):
#         # get user ID
#         bookID = input('Enter the ID of the book you want to borrow: ')

#         # # check in database 
#         available = mydb.borrow_book(str(self), bookID)
#         print(f'Abailable: {available}')
        

#         if available == None:
#             # print(f'{bookExist[0]} is currently not available!')
#             print(f'Book is currently not available!')

#      # return book
#     # def return_book(self):
#     #     # get user ID
#     #     bookID = input('Enter the ID of the book you want to return: ')

#     #     # # check in database 
#     #     return_book = mydb.return_book(str(self), bookID)
#     #     if return_book == None:
#     #         print('You did not borrow this book')
#     #     else:
#     #         print('Book returned successfully')



        
        



# # book1 = Book()
# # book1.search_by_anything()