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
    query = "SELECT cities.id, cities.name, states.name FROM cities, "
    query += "states WHERE BINARY state_id = states.id ORDER BY id ASC"
    cur.execute(query)
    datas = cur.fetchall()
    states = []

    for data in datas:
        if args in data:
            states.append(data[1])
    print(", ".join(states))

    cur.close()
    db.close()


if __name__ == "__main__":

    if len(sys.argv) < 5 or len(sys.argv) >= 6:
        print("Kindly provide in the following order: \t\nusername"
              "\t\npassword\t\ndatabase\nstate")
    else:
        dbConnectFunction(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
