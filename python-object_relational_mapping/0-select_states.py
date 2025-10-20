#!/usr/bin/python3
"""
Task 0: List all states from the database hbtn_0e_0_usa
Connects to MySQL using MySQLdb and prints all states sorted by id
"""

import MySQLdb
import sys


def get_states(username, password, dbname):
    """ Get all states from the database and print them sorted by id """
    try:
        with MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=dbname) as db:

            with db.cursor() as cursor:
                cursor.execute("SELECT * FROM states ORDER BY id ASC")
                # Fetch and display results
                results = cursor.fetchall()
                for row in results:
                    print(row)

    except MySQLdb.Error as error:
        print(f"MySQL Error: {error}")


if __name__ == "__main__":
    get_states(sys.argv[1], sys.argv[2], sys.argv[3])