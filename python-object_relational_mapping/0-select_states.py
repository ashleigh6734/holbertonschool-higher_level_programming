#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to fetch all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()