#!/usr/bin/python3

''' import sqlalchemy '''
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, String, Column, Integer, CHAR, MetaData
from model_state import Base, State
import sys


def alchemyFunction(user, pd, dbase):
    ''' function to connect to sqlalchemy and print
        output based on a search condition
    '''
    hst = "localhost"
    pt = 3306
    usr = user
    pwd = pd
    db = dbase

    engine = create_engine(f"mysql+mysqldb://{usr}:{pwd}@{hst}:{pt}/{db}")
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    session = Session(bind=engine)

    results = session.query(State).filter(
        State.name.contains("a")).order_by(State.id)
    for result in results:
        print(f"{result.id}: {result.name}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Please provide in the following order:"
              "\n\tUsername\n\tPassword\n\tDatabase Name")
    else:
        alchemyFunction(sys.argv[1], sys.argv[2], sys.argv[3])
