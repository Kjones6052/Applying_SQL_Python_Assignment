
# Importing database connection
from database_connection import connect_database

# Importing Error from MySQL Connector
from mysql.connector import Error

# Task 2: Add a Workout Session
# Develop a Python function to add a new workout session to the 'WorkoutSessions' table for a specific member.
def add_workout(session_id, member_id, session_date, session_time, activity): 
    # Establishing database connection
    conn = connect_database()

    # Checking for successful database connection
    if conn is not None:
        try:
            # Activating the cursor
            cursor = conn.cursor() 

            # Creating a new workout session
            new_workout = (session_id, member_id, session_date, session_time, activity)  

            # Query to add the new workout session
            query = "INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s, %s)" 

            # Executing the query
            cursor.execute(query, new_workout) 

            # Committing the changes to the database
            conn.commit()

            # Using a print statement to verify 
            print("New workout session added successfully.")
        
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