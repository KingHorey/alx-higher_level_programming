#!/usr/bin/python3

''' import sqlalchemy, sys and other submodules'''

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys


def alchemyFunction(user, pwd, dbase, args):
    ''' function creates a connection to the database, then returns output
    based on args based to it '''

    host = "localhost"
    port = 3306
    engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@{host}:"
                           f"{port}/{dbase}")

    Base.metadata.create_all(engine)
    # conn = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter(State.name ==
                                          sqlalchemy.sql.expression.bindparam(
                                              "input")).params(
                                              input=args).order_by(
        State.id).first()

    # results = session.query(State).filter(State.name == args).order_by(
    #     State.id)
    if results:
        print(results.id)
    else:
        print("Not found")


if __name__ == "__main__":
    alchemyFunction(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
