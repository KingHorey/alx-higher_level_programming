#!/usr/bin/python3

''' import sqlalchemy,sys and other important submodules'''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
# from sqlalchemy.engine import URL


def alchemyFunction(usr, passwd, dbase):
    ''' function inserts an object into the database'''
    host = "localhost"
    port = 3306

    engine = create_engine(f"mysql+mysqldb://{usr}:{passwd}@{host}:{port}/"
                           f"{dbase}")

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)

    louis = State(name="Louisiana")
    session.add(louis)
    session.commit()

    results = session.query(State).all()
    print(results[-1].id)


if __name__ == "__main__":
    alchemyFunction(sys.argv[1], sys.argv[2], sys.argv[3])
