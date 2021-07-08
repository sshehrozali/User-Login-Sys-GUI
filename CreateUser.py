# Import Libraries and functions
import hashlib
import sqlite3
from id_generator import make_id

def CreateNewAccount(first, last, number, email, password):
    
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

    # Generate NEW USER ID
    user_id = make_id(db_name, table1)

    # Insert "BIO-DATA"
    cursor.execute(f"INSERT INTO {table1} (ID, First_name, Last_name, Phone) VALUES(?, ?, ?, ?)", (user_id, first, last, number))
    connection.commit()

    # Insert "LOGIN-ID"
    cursor.execute(f"INSERT INTO {table2} (ID, Email, Password) VALUES(?, ?, ?)", (user_id, email, encrypted.hexdigest()))
    connection.commit()
    print("\nUSER CREATED SUCCESSFULLY\n")

    