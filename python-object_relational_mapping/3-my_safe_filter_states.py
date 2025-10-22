#!/usr/bin/python3
"""
Task 3: Safe filter states by user input
Connects to MySQL using MySQLdb and prevents SQL injection
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and search term from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor and execute the query safely using parameterized input
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC",
        (state_name,)
    )

    # Fetch and print matching rows
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()
