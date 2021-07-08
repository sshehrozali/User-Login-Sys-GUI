import tkinter

def access_granted(username):
    greetings = "Welcome, " + username
    
    LoginWindow = tkinter.Tk()                      # Creates new window
    LoginWindow.geometry("800x600")                 # Set resolution of the window
    LoginWindow.title(f"{username} Dashboard")      # Set title of the window
    LoginWindow.configure(bg="#1a2021")             # Set main window BG color

    # Creates greetings label
    GreetingsLabel = tkinter.Label(LoginWindow, text=greetings, bg="#1C1C21", fg="white", font=("Arial", 22)).grid(pady=50)

    LoginWindow.mainloop()