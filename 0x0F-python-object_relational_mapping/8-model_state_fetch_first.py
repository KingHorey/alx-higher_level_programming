#!/usr/bin/python3

''' import sqlalchemy and other important sub-modules'''

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, String, Column, create_engine
from model_state import State, Base
import sys


def alchemyFunction(usr, pwd, db_name):
    ''' function creates an engine and carries out queries on db\
            using ORM
    '''

    host = "localhost"
    port = 3306
    engine = create_engine(f"mysql+mysqldb://{usr}:{pwd}@{host}:{port}"
                           f"/{db_name}")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    search = session.query(State).order_by(State.id).first()
    if search:
        print(f"{search.id}: {search.name}")
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Please provide in the following order:"
              "\n\tUsername\n\tPassword\n\tDatabase Name")
    else:
        alchemyFunction(sys.argv[1], sys.argv[2], sys.argv[3])
