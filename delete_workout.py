# Importing database connection
from database_connection import connect_database

# Importing Error from MySQL Connector
from mysql.connector import Error

# Task 4: Delete a Workout Session
# Create a Python function to delete a workout session based on its session ID. Include error handling for cases where the session ID 
# does not exist.
def delete_workout(session_id, member_id):
    # Establishing database connection
    conn = connect_database()

    # Checking for successful database connection
    if conn is not None:
        try:
            # Activating the cursor
            cursor = conn.cursor() 

            # Creating the variable for removed_workout to be used later
            removed_workout = (session_id, member_id)

            # Query to delete a workout session
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s AND member_id = %s" 

            # Executing the query
            cursor.execute(query, removed_workout) 

            # Committing the changes to the database
            conn.commit()

            # Using a print statement to verify 
            print("Workout session successfully removed.")
        
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