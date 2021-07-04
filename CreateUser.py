# Import Libraries and functions
import hashlib
import sqlite3
from num1 import test_num
from email import test_email, email_search
from password import test_password
from alpha1 import test_alpha
from id_generator import make_id

# Filename for .db file [CHANGE HERE]
db_name = "data"
db_name1 = "login"

# Tables names for .db file [CHANGE HERE] [JUST DON'T USE '-']
table1 = "bio_data" # TABLE FOR USERS BIO DATA
table2 = "login_id" # TABLE FOR USERS LOGIN INFO
table3 = "login_info" # TABLE TO UPDATE LOGIN INFO

# Connections to sqlite3 db
connection = sqlite3.connect(f"DATABASE/{db_name}.db")  # DATABASE
connection1 = sqlite3.connect(f"LOGIN/{db_name1}.db")   # LOGIN

# Define cursors to sqlite3 db
cursor = connection.cursor()    # DATABASE
cursor1 = connection1.cursor()  # LOGIN

# CREATE tables (if not exists)
cursor.execute(f"CREATE TABLE IF NOT EXISTS {table1} (ID INTEGER, First_name TEXT, Last_name TEXT, Phone INTEGER)")
cursor.execute(f"CREATE TABLE IF NOT EXISTS {table2} (ID INTEGER, Email TEXT, Password TEXT)")
cursor1.execute(f"CREATE TABLE IF NOT EXISTS {table3} (ID INTEGER, First_name TEXT, Last_name TEXT, Last_login TEXT)")





# Function to create new User Account
def CreateNewAccount():
    print("\nCREATE NEW USER\n")

    #------------------------------------#
    #         CREATE NEW USER            #
    #------------------------------------#
    # Keep prompting till valid "FIRST NAME"
    while (True):

        first_name = input("\nEnter Your First Name: ")

        check = test_alpha(first_name)

        if check == True:
            break

        print("\nPlease Enter Correct First Name!\n")

    # Keep prompting till valid "LAST NAME"
    while (True):

        last_name = input("Enter Your Last Name: ")

        check = test_alpha(last_name)

        if check == True:
            break

        print("\nPlease Enter Correct Last Name!\n")

    # Keep promting till valid "EMAIL ID"
    while (True):

        email = input("Your Email ID: ")

        check1 = test_email(email)
        check2 = email_search(email, db_name, table2)

        if check1 == True and check2 == True:
            break

    # Keep promting till valid "PASSWORD"
    while (True):

        password = input("Your Password: ")

        check = test_password(password)

        if check == True:
            break

        print("\nPlease Enter Correct Password!\n")

    # Keep prompting till valid "PHONE NUMBER"
    while (True):

        phone_num = input("Enter Phone Number (+92): ")

        check = test_num(phone_num)

        if check == True:
            break

        print("\nPlease Enter Correct Phone Number!\n")

    # Encrypt Password (SHA224)
    encrypted = hashlib.sha224(password.encode())

    # Generate NEW USER ID
    user_id = make_id(db_name, table1)

    # Insert "BIO-DATA"
    cursor.execute(f"INSERT INTO {table1} (ID, First_name, Last_name, Phone) VALUES(?, ?, ?, ?)", (user_id, first_name, last_name, phone_num))
    connection.commit()

    # Insert "LOGIN-ID"
    cursor.execute(f"INSERT INTO {table2} (ID, Email, Password) VALUES(?, ?, ?)", (user_id, email, encrypted.hexdigest()))
    connection.commit()
    print("\nUSER CREATED SUCCESSFULLY\n")
    exit(0)

    if option != "1" and option != "2":
        print("\nPlease Enter Correct Option!\n")