from LibDatabase import LibDatabase 
from LibUser import Staff, Student, Librarian

# create instance of fatabase
myDatabase = LibDatabase()


class LibMgtSys:
    def __init__(self):
        
        # load books
        myDatabase.load_books()

        # display menu
        self.menu()


    # write the menu function
    def menu(self):

        while True:
             
            print("""
                  1. Register
                  2. Login
                  3. Incoming Option
                  q. Quit
                  
                  """) 
            
            # get user's input
            choice = input("Please select your option: ")

            f = {"1": self.register,
                 "2": self.login,
                 "3": self.incoming,
                 "q": None}.get(choice,None)            
           
           
            if choice == "q" or choice =="Q":
                break
            elif f == None:
                print("Try again...")
            else:
                f()
    
       
    # register function
    # @staticmethod
    def register(self):
        # print('REGISTER')

        # get user information
        print("""
            **************
            *  REGISTER  *
            **************
        """)
        user_type_list = ['librarian', 'staff', 'student']
        self.userID = input('Enter your ID : ')
        self.userType = input('Are you a Librarian, staff or a student?: ')
        self.username = input('Enter your username: ')
        self.password = input('Enter your password: ')

        while self.userType.lower() not in user_type_list:
            print('Wrong user type')
            self.userType = input('Are you a Librarian, staff or a student?: ')


        
        # save user info into database
        detail = myDatabase.register(self.userID, self.userType, self.username, self.password)
        if detail == True:
            # if the user is not a librarian, create an account automatically
            if self.userType !='librarian':
                myDatabase.create_account(self.userID)
        
            print(f'{self.username.capitalize()} has been registered.')
            
            # redirect to login function
            LibMgtSys.login(self)
        else:
            print(f'{self.username.capitalize()} or {self.userID} has been taken. Please Try again!')
            LibMgtSys.register(self)
        
        
    
    # # login function
    # @staticmethod
    def login(self):
        print(f"""
            **************
            *   LOGIN    *
            **************
        """)
        
        # let user enter usernamen and password
        self.username = input('Enter your username: ')
        self.password = input('Enter your password: ')

        # call the login function of the library management system
        user_details = myDatabase.login(self.username, self.password)

        
        if user_details:
            # instantiate user class
            # display menu for each user type
            #  'name', 'UserID', and 'StudentClass'
            if user_details[1] == 'student':
                student = Student(user_details[2],user_details[0], user_details[1])
                student.menu()
                
            elif user_details[1] == 'staff':
                staff = Staff(user_details[2],user_details[0], user_details[1])
                staff.menu()
                
            else:
                librarian = Librarian(user_details[2],user_details[0], user_details[1])
                librarian.menu()
                
           
        else:
            print('Incorrect username or password')
            # call login function again
            LibMgtSys.login(self)
            
        return user_details
   
            

    # logout function
    @staticmethod
    def logout():            
        # take user to the login function
        LibMgtSys.login()
    
    
    def incoming(self):
        print('This option is Incoming')

        
    # def __repr__(self):
    #     return self.username

   
    


# instantiate the library ,anagement system class
myLibrary = LibMgtSys()