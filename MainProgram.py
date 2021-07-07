# Funtion to open Create New Account Window
def Register():

    # Function to create New User Account
    def Create():

        # Class for New User
        class NewUser:
            # Initialization
            def __init__(self, FirstName, LastName, PhoneNumber, EmailAddress, Password):
                self.Firstname = FirstName
                self.Lastname = LastName
                self.Number = PhoneNumber
                self.Email = EmailAddress
                self.Password = Password
            
            ## GETTER METHODS ##
            def firstname(self):
                return self.Firstname

            def lastname(self):
                return self.Lastname

            def number(self):
                return self.Number

            def email(self):
                return self.Email

            def password(self):
                return self.Password

        # Create New User instance
        NewUserObj = NewUser("Ali", "Siddiqui", "033345678921", "ali123@gmail.com", "helloworld")

        # Call methods
        FIRSTNAME = NewUserObj.firstname()
        LASTNAME = NewUserObj.lastname()
        NUMBER = NewUserObj.number()
        EMAIL = NewUserObj.email()
        PASSWORD = NewUserObj.password()

        # PASSING THESE VALUES TO CreateNewAccount()
        CreateNewAccount(FIRSTNAME, LASTNAME, NUMBER, EMAIL, PASSWORD)


    ## CREATES A NEW WINDOW ##
    CreateUserWindow = tkinter.Tk()
    CreateUserWindow.geometry("700x500")
    CreateUserWindow.title("Create New Account")
    CreateUserWindow.configure(bg="#1a2021")

    ## HEADING ##
    CreateUserHeadingLabel = tkinter.Label(CreateUserWindow, text="Register your Account", fg="white", bg="#1a2021", font=("Open Sans", 26), anchor="center")    
    CreateUserHeadingLabel.grid(pady=20)
    
    # Declares variables for entry boxes
    firstname_var = tkinter.StringVar()
    lastname_var = tkinter.StringVar()
    number_var = tkinter.StringVar()
    email_var = tkinter.StringVar()
    password_var = tkinter.StringVar()
    confirmpassword_var = tkinter.StringVar()

    ## FIRST NAME FIELD ##
    FirstName_Label = tkinter.Label(CreateUserWindow, text="First Name", fg="white", bg="#1a2021", font=("Open Sans", 12))
    FirstName_Label.grid(column=0, row=1)
    FirstName_Input = tkinter.Entry(CreateUserWindow, textvariable=firstname_var)
    FirstName_Input.grid(column=1, row=1)

    ## LAST NAME FIELD ##
    LastName_Label = tkinter.Label(CreateUserWindow, text="Last Name", fg="white", bg="#1a2021", font=("Open Sans", 12))
    LastName_Label.grid(column=0, row=2)
    LastName_Input = tkinter.Entry(CreateUserWindow)
    LastName_Input.grid(column=1, row=2)

    ## PHONE NUMBER FIELD ##
    PhoneNumber_Label = tkinter.Label(CreateUserWindow, text="Phone Number", fg="white", bg="#1a2021", font=("Open Sans", 12))
    PhoneNumber_Label.grid(column=0, row=3)
    PhoneNumber_Input = tkinter.Entry(CreateUserWindow)
    PhoneNumber_Input.grid(column=1, row=3)

    ## EMAIL ADDRESS FIELD ##
    EmailAddress_Label = tkinter.Label(CreateUserWindow, text="Email Address", fg="white", bg="#1a2021", font=("Open Sans", 12))
    EmailAddress_Label.grid(column=0, row=4)
    EmailAddress_Input = tkinter.Entry(CreateUserWindow)
    EmailAddress_Input.grid(column=1, row=4)

    ## NEW PASSWORD FIELD ##
    Password_Label = tkinter.Label(CreateUserWindow, text="New Password", fg="white", bg="#1a2021", font=("Open Sans", 12))
    Password_Label.grid(column=0, row=5)
    Password_Input = tkinter.Entry(CreateUserWindow)
    Password_Input.grid(column=1, row=5)

    ## CONFIRM PASSWORD FIELD ##
    ConfirmPassword_Label = tkinter.Label(CreateUserWindow, text="New Password", fg="white", bg="#1a2021", font=("Open Sans", 12))
    ConfirmPassword_Label.grid(column=0, row=5)
    ConfirmPassword_Input = tkinter.Entry(CreateUserWindow)
    ConfirmPassword_Input.grid(column=1, row=5)
    
    Create_Btn = tkinter.Button(CreateUserWindow, text="Register", width=20, command=Create).grid(pady=30)    # Create new account button



####################
 ## MAIN PROGRAM ##
####################   
import tkinter                              # Import Tkinter Library
from CreateUser import CreateNewAccount     # Import CreateNewAccount() -> func
from LoginAccess import Login               # Import Login() -> func

window = tkinter.Tk()               # Creates main window object
window.geometry("400x300")          # Set window height and width
window.title("User Login System")   # Set main window title
window.configure(bg="#1a2021")      # Set main window BG color

## MAIN HEADING ##
Title_Label = tkinter.Label(window, text="User Login System", fg="white", bg="#1a2021", font=("Open Sans", 26))
Title_Label.pack(pady=20)

## CREATES LOGIN FIELD NAME WITH INPUT ##
Login_FieldNames = ["Email Address", "Password"]
for fieldnames in Login_FieldNames:
    Name = tkinter.Label(window, text=fieldnames, fg="white", bg="#1a2021", font=("Open Sans", 12)).pack()
    Input = tkinter.Entry(window).pack()

## LOGIN BUTTON ##
Login_Btn = tkinter.Button(text="Login", command=Login).pack(pady=20)

## CREATE NEW USER BUTTON ##
Create_User_Btn = tkinter.Button(text="Create Account", command=Register).pack()

window.mainloop()   # Creates main window loop