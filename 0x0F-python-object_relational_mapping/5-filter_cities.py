#!/usr/bin/python3
"""Module documentation """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ main function """
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities\
        INNER JOIN states ON states.id = cities.state_id\
        WHERE states.name = '%s'\
        GROUP BY cities.id" % argv[4])
    query_rows = cur.fetchall()
    s = ""
    for row in query_rows:
        s += row[0]
        if row[0] not in query_rows[len(query_rows) - 1]:
            s += ', '
    print(s)
    cur.close()
    conn.close()
