# Importing database connection
from database_connection import connect_database

# Importing Error from MySQL Connector
from mysql.connector import Error

# Task 3: Updating Member Information
# Implement a function to update the age of a member. Ensure that your function checks if the member exists before attempting the update
def update_member_age(member_id, age):
    # Establishing database connection
    conn = connect_database()

    # Checking for successful database connection
    if conn is not None:
        try:
            # Activating the cursor
            cursor = conn.cursor()  

            # Creating the variable for update_member to use later
            update_member = (age, member_id)

            # Query to update a member's age
            query = "UPDATE Members SET age = %s WHERE id = %s" 

            # Executing the query
            cursor.execute(query, update_member) 

            # Committing the changes to the database
            conn.commit()

            # Using a print statement to verify 
            print("Member age updated successfully.")
        
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