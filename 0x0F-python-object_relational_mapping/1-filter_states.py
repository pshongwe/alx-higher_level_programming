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
    cur.execute("""SELECT * FROM states where name
                like BINARY 'N%' ORDER BY states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
