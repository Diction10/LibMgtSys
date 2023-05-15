import sqlite3
import json
from datetime import datetime, timedelta


class LibDatabase:

    def __init__(self):
        # create database Library Mgt Sys
        self.con = sqlite3.connect("LibrarySystem2.db")

        # create a cursor
        self.cur = self.con.cursor()

        # create table for library users
        self.cur.execute("""CREATE TABLE IF NOT EXISTS  users(
            userID INTEGER UNIQUE,
            user_type text,
            username text PRIMARY KEY,
            password text
            )""")
        
        # create table books
        self.cur.execute("""CREATE TABLE IF NOT EXISTS  books(
            BookID INTEGER PRIMARY KEY,
            title text,
            authors text,
            lang_code text,
            published_date DATE,
            available_books INTEGER
            )""")

        # create table for library users
        self.cur.execute("""CREATE TABLE IF NOT EXISTS  account(
            userID INTEGER,
            Fine INTEGER DEFAULT 0,
            FOREIGN KEY(userID) REFERENCES users(userID)
            )""")
        
        # create table borrowed books
        self.cur.execute("""CREATE TABLE IF NOT EXISTS  borrowed_books(
            BookID INTEGER,
            userID INTEGER,
            date_borrowed DATE,
            due_date DATE,
            FOREIGN KEY(BookID) REFERENCES books(BookID),
            FOREIGN KEY(userID) REFERENCES users(userID)          
            )""")
        
        # create table returned books
        self.cur.execute("""CREATE TABLE IF NOT EXISTS  returned_books(
            BookID INTEGER,
            userID INTEGER,
            date_returned DATE,
            FOREIGN KEY(BookID) REFERENCES books(BookID),
            FOREIGN KEY(userID) REFERENCES users(userID)          
            )""")
        
        # create table reserved books
        self.cur.execute("""CREATE TABLE IF NOT EXISTS  reserved_books(
            BookID INTEGER,
            userID INTEGER,
            date_reserved DATE,
            expiry_date DATE,
            FOREIGN KEY(BookID) REFERENCES books(BookID),
            FOREIGN KEY(userID) REFERENCES users(userID)          
            )""")
        
        # create table book history
        self.cur.execute("""CREATE TABLE IF NOT EXISTS  book_history(
            UserID INTEGER,
            BookID INTEGER,
            is_Added INTEGER,
            is_Borrowed INTEGER,
            is_Returned INTEGER,
            Date DATE,
            FOREIGN KEY(BookID) REFERENCES books(BookID),
            FOREIGN KEY(userID) REFERENCES users(userID)          
            )""")
    

    # load book functions
    # @staticmethod
    def load_books(self):

        try:

            with open("books.json", encoding="utf-8" ) as fd:
                books = json.load(fd)
    
            for book in books:
                # save to db
                self.cur.execute("""INSERT INTO books VALUES(:BookID, :title, :authors, 
                    :lang_code, :pub_date, :num_of_book)""",
                    {'BookID':book['bookID'], 'title':book['title'], 
                    'authors':book['authors'], 'lang_code':book['language_code'],                     
                    'pub_date':book['publication_date'], 'num_of_book':5 })

        except sqlite3.IntegrityError:
            pass

        # # commit into dtatbase
        self.con.commit()

        # # self.cur.close()
        # self.con.close()
            
            
        
    # register user to database
    def register(self, userID, userType, username, password):
        
        try:
            # save to db
            self.cur.execute("INSERT INTO users VALUES(:userID, :user_type, :username, :password)",
                        {'userID':userID, 'user_type':userType.lower(), 'username':username.lower(), 'password':password})
            # commit and save query
            self.con.commit()
            return True
        
        except sqlite3.IntegrityError:
            # print(f'{username.capitalize()} or {userID} has been taken. Please choose another')
            return False

    
    # create account for users
    def create_account(self, userID):

        # save to db
        self.cur.execute("INSERT INTO account VALUES(:userID, :Fine)",
                    {'userID':userID, 'Fine':0})
        
        # commit and save query
        self.con.commit()
        
    
    # login authentication
    def login(self, username, password):
        # check if the credentials exists in the database
        self.cur.execute(""" 
                    select * from users
                    where users.username = :username
                    and users.password = :password
                    """,{'username':username.lower(), 'password' : password})
        
        credentials = self.cur.fetchone()

        # authenticate user
        if credentials:
            return credentials
        # else:
        #     return None
        
        # self.cur.close()
        # self.con.close()

       
                
    # verify user
    def verify(self, userID):
        """
        Get a user ID 
        Check if the user exists in the system
        Might not necessarily be used by all of the subclass
        # Let the user eneter their department fr staff and class for student
        """

        # query the database and see if it exists
        # check if the credentials exists in the database
        self.cur.execute(""" 
                    select users.username, users.userID from users
                    where users.userID = :userID
                    """,{'userID':userID})
            
        credentials = self.cur.fetchone()
       
        # authenticate user
        if credentials:
            return credentials


  

    
    # insert book and save to the database
    def insert_book(self, userID, bookID, title, author, language, pub_year):
         # save to db
        self.cur.execute("INSERT INTO books VALUES(:BookID, :title, :authors, :lang_code, :published_date, :available_books)",
                    {'BookID':bookID,'title':title, 'authors':author, 
                     'lang_code':language,'published_date':pub_year,
                     'available_books':5})
        
        # update book history
        self.cur.execute("INSERT INTO book_history VALUES(:UserID, :BookID, :is_Added, :is_Borrowed, :is_Returned,:Date)",
                    {'UserID':userID,'BookID':bookID,'is_Added':1, 'is_Borrowed':0, 
                     'is_Returned':0,'Date':datetime.now()})
        
        # commit and save query
        self.con.commit()
    
    
    # search book by title
    def search_by_anything(self, data):

        data = '%'+data+'%'
        self.cur.execute(""" 
                  select BookID, title,authors,lang_code,published_date from books
                  where title like :d
                  or authors like :d
                  or lang_code like :d
                  or published_date like :d                
                  """,{'d':data})
        result = self.cur.fetchall()

        if result != None:
            return result 
        else:
            return None  
 
        
    
    # seearch book function
    def search_book(self, BookID):

        # get a book info by its ID
        self.cur.execute(""" 
                    select books.title, books.available_books, books.authors from books where books.bookID = :bookID
                    """,{'bookID':BookID})
        
        available = self.cur.fetchone()

        if available:
            return available
        else:
            return None
    
    # update book
    def update_book(self, BookID, Book_Count):
        # update availability column on books table
        self.cur.execute("""update books set available_books = :available where bookID = :bookID
                    """,{'available':Book_Count,'bookID' :BookID })
        
        # commit into and close db
        self.con.commit()
        # self.cur.close()
        # self.con.close()
        
    
    # display book
    def display_book(self):
        print('Display Book')

    
    # borrowed books
    def borrow_book(self, userID, bookID):
        
        # check if book exists
        bookExist = LibDatabase.search_book(self, bookID)

        # check if user has already borrowed book
        self.cur.execute("""Select userID, BookID FROM  borrowed_books WHERE userID = :userID and bookID = :bookID
            """,{'userID':userID,'bookID' :bookID })
        
        details = self.cur.fetchone()
        
        if details != None:
            return False
        else:
            # check if book exists and is available
            if bookExist and bookExist[1] > 0:
                # borrow user book and save to database of borrowed books
                self.cur.execute("INSERT INTO borrowed_books VALUES(:BookID, :userID, :date_borrowed, :due_date)",
                        {'BookID':bookID, 'userID':userID, 
                            'date_borrowed':datetime.now(), 
                            'due_date':datetime.now() + timedelta(seconds=20)})
            
                # decreas book count by 1
                new_available = bookExist[1] - 1

                # update availability column on books table
                self.cur.execute("""update books set available_books = :available where bookID = :bookID
                        """,{'available':new_available,'bookID' :bookID })
                
                
                # update book history
                self.cur.execute("INSERT INTO book_history VALUES(:UserID, :BookID, :is_Added, :is_Borrowed, :is_Returned, :Date)",
                            {'UserID':userID,'BookID':bookID,'is_Added':0, 
                            'is_Borrowed':1, 'is_Returned':0,'Date':datetime.now()})
                
                # commit into and close db
                self.con.commit()
                return True
            else:
                return None
              

    # return book function
    def return_book(self, userID, bookID):

        # check if user borrowed book to be returned
        self.cur.execute(""" 
            select userID, BookID from borrowed_books
            where UserID = :userID and BookID = :BookID
            """,{'userID':userID, 'BookID':bookID})
        
        # get lists of books borrowed by the user
        borrowed_books = self.cur.fetchone()

        if borrowed_books != None:
            # if bookid is in list of borrowed books
            if bookID == str(borrowed_books[1]):
                # check for fine
                LibDatabase.fine(self, userID, bookID)

                # return books
                self.cur.execute("INSERT INTO returned_books VALUES(:BookID, :userID, :date_returned)",
                        {'BookID':bookID, 'userID':userID, 'date_returned':datetime.now()})

                # get book count
                bookExist = LibDatabase.search_book(self, bookID)
                
                # update availability column on books table
                self.cur.execute("""update books set available_books = :available where bookID = :bookID
                        """,{'available':bookExist[1] + 1,'bookID' :bookID })
                
                # update book history
                self.cur.execute("INSERT INTO book_history VALUES(:UserID, :BookID, :is_Added, :is_Borrowed, :is_Returned, :Date)",
                            {'UserID':userID,'BookID':bookID,'is_Added':0, 
                            'is_Borrowed':0, 'is_Returned':1,'Date':datetime.now()})
                
                # delete book from borrowed table
                self.cur.execute("""Delete FROM  borrowed_books WHERE userID = :userID and bookID = :bookID
                    """,{'userID':userID,'bookID' :bookID })
                
                # commit into and close db
                self.con.commit()
                return True
        else:
            return None

       
    # reserve books db logic
    def reserve_book(self, userID, bookID):
        # check if book exists
        bookExist = LibDatabase.search_book(self, bookID)

        # check if book exists and is available
        if bookExist and bookExist[1] > 0:

            #store reserved books in reserved table
            self.cur.execute("INSERT INTO reserved_books VALUES(:BookID, :userID, :date_reserved, :expiry_date)",
                    {'BookID':bookID, 'userID':userID, 
                        'date_reserved':datetime.now(), 
                        'expiry_date':datetime.now() + timedelta(days=5)})
        
            # decreas book count by 1
            new_available = bookExist[1] - 1

            # update availability column on books table
            self.cur.execute("""update books set available_books = :available where bookID = :bookID
                    """,{'available':new_available,'bookID' :bookID })
            
            # commit into and close db
            self.con.commit()
            return True
        else:
            return False
    
    # book history
    def book_history(self, date):
        # query db history
        self.cur.execute(""" 
                    select * from book_history where Date <= :date
                    """,{'date':date})
        
        details = self.cur.fetchall()

        if details:
            return details
        else:
            return None
        
    # fine calculation and imposition
    def fine(self, userID, BookID):
        # get the due date they borrowed the book
        self.cur.execute(""" 
                    select due_date from borrowed_books where userID = :userID and BookID = :BookID
                    """,{'userID':userID, 'BookID':BookID})
        detals = self.cur.fetchone()

        due_date = detals[0]

        # today = datetime.strptime(datetime.now(), "%Y/%m/%d")
        due_date = datetime.strptime(due_date, "%Y-%m-%d %H:%M:%S.%f")    
        today = datetime.now()
        time_difference = due_date - today
        print(time_difference.seconds)

        if time_difference.total_seconds() < 0:
        
            # user pays 1p per second
            fine_payment = -time_difference.total_seconds() * 1

            # update user account
            self.cur.execute("""update account set Fine = :Fine where userID = :userID
                        """,{'Fine':fine_payment,'userID' :userID })
        
            self.con.commit()
        
     


        
                