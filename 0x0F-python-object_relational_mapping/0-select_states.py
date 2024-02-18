#!/usr/bin/python3
''' Import MySQLdb module to connect and interact with database '''

import MySQLdb
import sys


def dbConnectFunction(usrn, pwd, dbase):

    dbse = MySQLdb.connect(user=usrn, passwd=pwd,
                           db=dbase, port=3306, host="localhost",
                           charset="utf8")
    cur = dbse.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    datas = cur.fetchall()

    for data in datas:
        print(data)

    cur.close()
    dbse.close()


if __name__ == "__main__":
    dbConnectFunction(sys.argv[1], sys.argv[2], sys.argv[3])
