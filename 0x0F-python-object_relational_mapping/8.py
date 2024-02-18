#!/usr/bin/python3

""" import sys for command line argument
    import sqlalchemy
    import 
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, CHAR, String
from model_state import Base, State
import sqlalchemy as db


def create_engine(usr, pwd, dbase):

    port = 3306
    host = "localhost"
    engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}".format(usr, pwd, host, port, dbase))
    return create_engine

def connect_engine(ngin):
    """ connect to the engine """
    start = ngin.connect

    return (start)

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    dbase = sys.argv[3]

    engine_create = create_engine(user, password, dbase)
    connection = connect_engine(engine_create)
    metadata = db.MetaData()
    Base.metadata.create_all(bind=engine_create)
    Session = sessionmaker()
    session = Session(bind=engine_create)
    
