#!/usr/bin/python3
"""
Task 0: List all states from the database hbtn_0e_0_usa
Connects to MySQL using MySQLdb and prints all states sorted by id
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name)

    # Create a cursor and execute the query
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all rows
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()
