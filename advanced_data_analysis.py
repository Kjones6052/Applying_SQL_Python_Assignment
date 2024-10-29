# Importing database connection
from database_connection import connect_database

# Importing Error from MySQL Connector
from mysql.connector import Error

# Establishing the database connection
conn = connect_database()

# Task 1: SQL BETWEEN Usage
# Retrieve the details of members whose ages fall between 25 and 30.

if conn is not None:
    try:
        # Activate the cursor
        cursor = conn.cursor()

        # Defining the query to fetch members with ages between 25 and 30
        query = """
            SELECT * FROM Members
            WHERE age BETWEEN 25 AND 30;
        """

        # Executing the query
        cursor.execute(query)

        # Displaying the data fetched by the query
        for member in cursor.fetchall():
            print(member)

    # General Exception Handling
    except Exception as ge:
        print(f"General Error Occurred: {ge}")

    # Database Error Handling
    except Error as dbe:
        print(f"Database Error Occurred: {dbe}")

    # Closing the cursor and connection
    finally:
        cursor.close()
        conn.close()