# Import Libraries and functions
import hashlib
import sqlite3
from id_generator import make_id

def Login():

    email = "ali123@gmail.com"
    password = "helloworld"

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

    # Encrypt Password (SHA224)
    encrypted = hashlib.sha224(password.encode())

    # SELECT "PASSWORD" of that "EMAIL ID"
    user_id = cursor.execute(f"SELECT Password from {table2} WHERE Email = ?", (email, encrypted.hexdigest()))
    
    # Fetch response
    user_check = user_id.fetchone()

    if user_check != None:
        
        # If Password matches
        if encrypted.hexdigest() == user_check[0]:
            
            # Get First and Last name of USER
            info = cursor.execute(f"SELECT First_name, Last_name from {table1} WHERE ID = (SELECT ID from {table2} WHERE Email = ? AND Password = ?)", (email, encrypted.hexdigest()))

            # Fetch response
            user_info = info.fetchall()

            print("Logged In")
