#!/usr/bin/python3

''' import MySQLdb for connecting to DB
    import sys for commandline arguments
'''

import MySQLdb as mdb
import sys


def dbConnectFunction(usr, pwd, dbase, args):
    """ function that connects to the database
    and carries out tasks based on queries """

    hst = "localhost"
    dbse = dbase
    prt = 3306
    dbs = mdb.connect(user=usr, passwd=pwd, db=dbse, port=prt,
                      host=hst, charset="utf8")
    cur = dbs.cursor()

    query = "SELECT * from states WHERE BINARY "
    query += "name = '{}' ORDER BY id ASC".format(args)
    cur.execute(query)
    datas = cur.fetchall()
    for data in datas:
        print(data)

    cur.close()
    dbs.close()


if __name__ == "__main__":
    dbConnectFunction(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
