# Funtion to open Create New Account Window
from tkinter import font


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

        # Initiate the user about event went successful -> Append new label inside Register window
        Created_Label = tkinter.Label(CreateUserWindow, text="Account Created successfully", bg="#1c1c21", fg="white", font=("Arial", 18))
        Created_Label.grid()

    ## CREATES A NEW WINDOW ##
    CreateUserWindow = tkinter.Tk()
    CreateUserWindow.geometry("700x500")
    CreateUserWindow.title("Create New Account")
    CreateUserWindow.configure(bg="#1a2021")

    ## HEADING ##
    CreateUserHeadingLabel = tkinter.Label(CreateUserWindow, text="Register your Account", fg="white", bg="#1a2021", font=("Open Sans", 26), anchor="center")    
    CreateUserHeadingLabel.grid(pady=20)

    ## CREATE LABELS AND INPUTS FIELDS ##
    rowCounter = 1  # Counter to count number of rows`  
    labels = ["First Name", "Last Name", "Phone Number", "Email Address", "Password"]
    for label in labels:
        Label = tkinter.Label(CreateUserWindow, text=label, fg="white", bg="#1a2021", font=("Open Sans", 12)).grid(column=0, row=rowCounter)
        Input = tkinter.Entry(CreateUserWindow).grid(column=1, row=rowCounter)
        rowCounter += 1     # Increament row counter

    # Create New Account Button    
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