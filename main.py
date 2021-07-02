def CreateUser():

    ## CREATES A NEW WINDOW ##
    CreateUserWindow = tkinter.Tk()
    CreateUserWindow.geometry("400x500")
    CreateUserWindow.title("Create New Account")
    CreateUserWindow.configure(bg="#1a2021")

    ## HEADING ##
    CreateUserHeadingLabel = tkinter.Label(CreateUserWindow, text="Register your Account", fg="white", bg="#1a2021", font=("Open Sans", 26), anchor="center")
    CreateUserHeadingLabel.grid(row=0)

    ## FIRST NAME FIELD ##
    FirstName_Label = tkinter.Label(CreateUserWindow, text="First Name", fg="white", bg="#1a2021", font=("Open Sans", 12))
    FirstName_Label.grid(column=0, row=1)
    FirstName_Input = tkinter.Entry(CreateUserWindow)
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

    ## NEW PASSWOR FIELD ##
    Password_Label = tkinter.Label(CreateUserWindow, text="New Password", fg="white", bg="#1a2021", font=("Open Sans", 12))
    Password_Label.grid(column=0, row=5)
    Password_Input = tkinter.Entry(CreateUserWindow)
    Password_Input.grid(column=1, row=5)


import tkinter                      # Import Tkinter Library

window = tkinter.Tk()               # Creates main window object
window.geometry("400x300")          # Set window height and width
window.title("User Login System")   # Set main window title
window.configure(bg="#1a2021")      # Set main window BG color

## MAIN HEADING ##
Title_Label = tkinter.Label(window, text="User Login System", fg="white", bg="#1a2021", font=("Open Sans", 26))
Title_Label.pack(pady=20)



## EMAIL FIELD ##
UserEmail = tkinter.Label(window, text="Email Address", fg="white", bg="#1a2021", font=("Open Sans", 12)).pack()
UserEmailInput = tkinter.Entry(window).pack()

## PASSWORD FIELD ##
UserPassword = tkinter.Label(window, text="Password", fg="white", bg="#1a2021", font=("Open Sans", 12)).pack()
UserPasswordInput = tkinter.Entry(window).pack()

# LOGIN BUTTON
Login_Btn = tkinter.Button(text="Login").pack(pady=20)



## CREATE NEW USER BUTTON ##
Create_User_Btn = tkinter.Button(text="Sign Up", command=CreateUser).pack()

window.mainloop()   # Creates main window loop