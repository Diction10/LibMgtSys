import sqlite3
from LibMgtSys import myDatabase

class Account:
    def __init__(self, num_borrowed_books=None, num_reserved_books=None, 
                 num_returned_books=None, num_lost_books = None, fine_amount=0):
         
        self.fine_amount = fine_amount
        self.borrowed_books = num_borrowed_books
        self.reserved_books = num_reserved_books
        self.returned_books = num_returned_books
        self.lost_boks = num_lost_books
    

    
    
    # user starting account
    def initialize_account(self):
        borrowed_books= self.borrowed_books
        reserved_books = self.reserved_books
        returned_books = self.returned_books
        fine = self.fine_amount = 0



        print (f"""
        *****************************
        * ACCOUNT FOR                *
        *****************************
        Books Borrowed = {borrowed_books}
        Reserved Books = {reserved_books}
        Returned Books = {returned_books}
        Your fine amount is ${fine}
        """)

        

    # calculate fine function
    def calculate_fine(self):
        pass

    
    def __repr__(self):
        return self.fine_amount