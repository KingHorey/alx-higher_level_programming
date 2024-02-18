#!/usr/bin/python3

''' Import MySQLdb for connection and activity on database
    import sys for command-line arguments.
'''

import MySQLdb as mdb
import sys


def dbConnectFunction(usr, pwd, dbase, args):
    ''' function creates a connection to the database and
    carries out a search query on the database
    '''
    hst = "localhost"
    db = mdb.connect(user=usr, passwd=pwd, db=dbase, port=3306, host=hst,
                     charset="utf8")
    cur = db.cursor()
    query = "SELECT * from states WHERE BINARY name=%s ORDER BY id ASC"
    cur.execute(query, (args,))
    datas = cur.fetchall()

    for data in datas:
        print(data)

    cur.close()
    db.close()


if __name__ == "__main__":
    dbConnectFunction(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
