#!/usr/bin/python3
"""Lists filtered states from database"""
import sys
import MySQLdb

if __name__ == "__main__":
    h = "localhost"
    u = sys.argv[1]
    pswd = sys.argv[2]
    d = sys.argv[3]
    p = 3306
    db = MySQLdb.connect(host=h, user=u, passwd=pswd, db=d, port=p)
    cur = db.cursor()
    state = sys.argv[4]
    cur.execute("""SELECT cities.name
                FROM cities INNER JOIN states
                ON states.id = cities.state_id
                WHERE states.name = %s """, (state,))
    rows = cur.fetchall()
    new_rows = list(r[0] for r in rows)
    print(*new_rows, sep=", ")
    cur.close()
    db.close()
