import sqlite3
import csv

#this connects to the database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

#this will create the table with the users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    fname TEXT,
    ename TEXT,
    epost TEXT,
    tlf TEXT,
    postnummer INTEGER
)
''')

#this is the file path that containes the users data
filename = "C:/Users/yasch/Downloads/Listeforad.csv"

#it will read the data from the csv file and put it into the database
def insert_data_from_csv(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('''
            INSERT INTO users (fname, ename, epost, tlf, postnummer)
            VALUES (?, ?, ?, ?, ?)
            ''', (row['fname'], row['ename'], row['epost'], row['tlf'], row['postnummer']))
    conn.commit()
    print("Data inserted successfully.")

#this function will insert the data from the csv file
insert_data_from_csv(filename)

#my function to search for a user
def search_user():
    firstnamevar = input("Enter the first name: ")
    lastnamevar = input("Enter the last name: ")
    cursor.execute('''
    SELECT * FROM users WHERE fname = ? AND ename = ?
    ''', (firstnamevar, lastnamevar))
    result = cursor.fetchone()
    if result:
        print("Name:", result[1], result[2])
        print("Email:", result[3])
        print("Telephone:", result[4])
        print("Postnumber:", result[5])
    else:
        print("User not found")

#my function to add a user
def add_user():
    firstname = input("Enter the first name: ")
    lastname = input("Enter the last name: ")
    email = input("Enter the email address: ")
    tlf = input("Enter the telephone number: ")
    postnumber = input("Enter the post number: ")
    cursor.execute('''
    INSERT INTO users (fname, ename, epost, tlf, postnummer)
    VALUES (?, ?, ?, ?, ?)
    ''', (firstname, lastname, email, tlf, postnumber))
    conn.commit()
    print("User added successfully.")

#my function to delte a user
def delete_user():
    firstname = input("Enter the first name of the user you want to delete: ")
    lastname = input("Enter the last name of the user you want to delete: ")
    cursor.execute('''
    DELETE FROM users WHERE fname = ? AND ename = ?
    ''', (firstname, lastname))
    conn.commit()
    print("User deleted successfully.")

#this is the menu for users to pick from
def main_menu():
    print("Main Menu:")
    print("1. Search User")
    print("2. Add User")
    print("3. Delete User")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        search_user()
    elif choice == '2':
        add_user()
    elif choice == '3':
        delete_user()
    elif choice == '4':
        print("Exiting...")
        conn.close()
        exit()
    else:
        print("Invalid choice. Please enter a valid option.")

#this will call the function on a loop
while True:
    main_menu()


