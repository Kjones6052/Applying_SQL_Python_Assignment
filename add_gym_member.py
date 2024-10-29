# Importing database connection
from database_connection import connect_database

# Importing Error from MySQL Connector
from mysql.connector import Error

# Task 1: Add a Member
# Write a Python function to add a new member to the 'Members' table in the gym's database.
def add_member(id, name, age):
    # Establishing database connection
    conn = connect_database()

    # Checking for successful database connection
    if conn is not None:
        try:
            # Activating the cursor
            cursor = conn.cursor() 

            # Creating a new member
            new_member = (id, name, age)  

            # Query to add the new member
            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)" 

            # Executing the query
            cursor.execute(query, new_member) 

            # Committing the changes to the database
            conn.commit()

            # Using a print statement to verify 
            print("New customer added successfully.")
        
        # General Exception Handling
        except Exception as ge:
            print(f"General Error Occurred: {ge}")

        # Database Error Handling
        except Error as dbe:
            print(f"Database Error Occurred: {dbe}")

        # Closing the connection and cursor
        finally: 
            cursor.close()
            conn.close()