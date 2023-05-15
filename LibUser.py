# from LibMgtSys import myDatabase
from LibDatabase import LibDatabase
from Books import Book

class LibUser:
    def __init__(self, name, UserID):
        self.name = name
        self.UID = UserID

    
    # verify function
    def verify(self):
        """
        Get a user ID 
        Check if the user exists in the system
        Might not necessarily be used by all of the subclass
        # Let the user eneter their department fr staff and class for student
        """

        # get the userID of the user
        userID = input('What is your user ID: ?')
        result = LibDatabase.verify(self, userID)
        if result:
            print(f'Welcome {result[0]}')
        else:
             print('User does not exist!')
      
            
        

    # check acount function
    def CheckAccount(self):
        """
        Get the Account info of this particular user
        """
        print('This is your account')
        # print(Account().initial_account())


    # get book information function
    def GetBookInfo(self):
        """
        Get the info abut any particular book entered
        """
        print('Book')

    
    # def __repr__(self):
    #     return self.name
    

# Student class
class Student(LibUser):
    def __init__(self, name, UserID, StudentClass):
        super().__init__(name, UserID)
        # self.StudentClass = StudentClass
        self.book = Book(UserID)
        self.name = name
    
        
    # student menu
    def menu(self):
        print(f"""
        
            * WELCOME {self.name.upper()} *
            
            """)
        
        while True:
             
            print("""
                  1. Borrow Book
                  2. Return Book
                  3. Reserve Book
                  4. View Book
                  5. Search Book
                  q. Quit
                  
                  """) 
            
            # get user's input
            choice = input("Please select your option: ")

            f = {"1": self.book.borrow_book,
                 "2": self.book.return_book,
                 "3": self.book.reserve_book,
                 '4': self.book.view_book,
                 '5': self.book.search_by_anything,
                 "q": None}.get(choice,None)
           
           
            if choice == "q" or choice =="Q":
                break
            elif f == None:
                print("Try again...")
            else:
                f()
    
    
    # def __repr__(self):
    #     return self.StudentClass

    
# Staff class
class Staff(LibUser):
    def __init__(self, name, UserID, Department):
        # super().__init__(name, UserID)
        # self.Department = Department
        self.book = Book(UserID)
        self.name = name
        self.menu()

    # staff menu
    def menu(self):
        print(f"""
            
            * WELCOME {self.name.upper()} *
            
        """)
        
        while True:
             
            print("""
                   1. Borrow Book
                  2. Return Book
                  3. Reserve Book
                  4. View Book
                   5. Search Book
                  q. Quit
                  """) 
            
            # get user's input
            choice = input("Please select your option: ")

            f = {"1": self.book.borrow_book,
                 "2": self.book.return_book,
                 "3": self.book.reserve_book,
                 '4': self.book.view_book,
                 '5': self.book.search_by_anything,
                 "q": None}.get(choice,None)
           
            if choice == "q" or choice =="Q":
                break
            elif f == None:
                print("Try again...")
            else:
                f()
    
    
    # def __repr__(self):
    #     return self.Department
    

# Librarian class
class Librarian(LibUser):
    def __init__(self, name, UserID, search_string):
        super().__init__(name, UserID)
        # self.search_string = search_string
        self.book = Book(UserID)
        self.name = name
        self.menu()
    
    # librarian menu
    def menu(self):
        print(f"""
        
        * WELCOME {self.name.upper()} *
        
        """)
        
        while True:
            print("""
                1. View Books
                2. Enter New Book
                3. Edit Book
                4. View History
                5. Search Books by Date, Language or Author
                q. Quit
            """)

            choice = input('Please Select your options: ')

            f = {'1': self.book.view_book,
                 '2': self.book.insert_book,
                 '3': self.book.update_book,
                 '4': self.book.book_history,
                 '5': self.book.search_by_anything,
                 'q': 'Quit'}.get(choice)

            if choice == 'q' or choice == 'Q':
                break
            elif f == None:
                print('Please try again')
            else:
                f()      
           
    
    # def __repr__(self):
    #     return self.Department
    