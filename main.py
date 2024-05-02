import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    firstname TEXT,
    lastname TEXT,
    email TEXT,
    postnumber INTEGER
)
''')

# Sample data to insert into the users table
data = [
    ('John', 'Doe', 'john.doe@example.com', 12345),
    ('Jane', 'Smith', 'jane.smith@example.com', 54321),
    ('Bob', 'Johnson', 'bob.johnson@example.com', 98765)
]

# Insert sample data into the users table
cursor.executemany('''
INSERT INTO users (firstname, lastname, email, postnumber)
VALUES (?, ?, ?, ?)
''', data)

# Function to search for a user
def search_user():
    firstnamevar = input("Enter the first name: ")
    lastnamevar = input("Enter the last name: ")
    cursor.execute('''
    SELECT * FROM users WHERE firstname = ? AND lastname = ?
    ''', (firstnamevar, lastnamevar))
    result = cursor.fetchone()
    if result:
        print("Name:", result[1], result[2])
        print("Email:", result[3])
        print("Postnumber:", result[4])
    else:
        print("User not found")

# Function to add a user
def add_user():
    firstname = input("Enter the first name: ")
    lastname = input("Enter the last name: ")
    email = input("Enter the email address: ")
    postnumber = input("Enter the post number: ")
    cursor.execute('''
    INSERT INTO users (firstname, lastname, email, postnumber)
    VALUES (?, ?, ?, ?)
    ''', (firstname, lastname, email, postnumber))
    conn.commit()
    print("User added successfully.")

# Function to delete a user
def delete_user():
    user_id = input("Enter the ID of the user you want to delete: ")
    cursor.execute('''
    DELETE FROM users WHERE id = ?
    ''', (user_id,))
    conn.commit()
    print("User deleted successfully.")

# Main menu function
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

# Main loop
while True:
    main_menu()


