#!/usr/bin/python3
"""
Defines a function that filters all states with a name starting with N
"""


import sys
import MySQLdb


def filter_states(username, password, database):
    """
    Filters all states with a name staring with N from a database
    """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = conn.cursor()
    cursor.execute(
        "SELECT states FROM * WHERE name LIKE 'N%' ORDER BY id ASC"
        )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    username  = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    filter_states(username, password, database)