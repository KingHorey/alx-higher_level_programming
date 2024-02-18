#!/usr/bin/python3

""" Import sys
    import sqlalchemy and other methods
    import state and base class
"""

import sys
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, String, CHAR, Column, create_engine
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base


def dbconnect(usr, pwd, dbase):
    """ create engine to connect to database """
    port = 3306
    host = "localhost"

    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(usr,
                                                                   pwd,
                                                                   host, port,
                                                                   dbase))
    return engine


def connect_engine(ngin):
    """ connect the created engine to db"""
    engine_connect = ngin.connect()
    return engine_connect


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    dbase = sys.argv[3]

    db_ngin = dbconnect(user, pwd, dbase)
    connect = connect_engine(db_ngin)
    metadata = db.MetaData()

    Base.metadata.create_all(bind=db_ngin)

    Session = sessionmaker(bind=db_ngin)
    session = Session()

    session.commit()
    search = session.query(State).order_by(State.id)

    for result in search:
        print("{}: {}".format(result.id, result.name))
