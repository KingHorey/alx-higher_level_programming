#!/usr/bin/python3

''' import sqlalchemy, sys and other import sqlalchemy submodules '''
import sys
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sqlalchemy import create_engine, update


def alchemyFunction(user, passwd, dbase):
    ''' function connects to the database and renames an object in the
    table based on id '''

    host = "localhost"
    port = 3306
    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@{host}:"
                           f"{port}/{dbase}")

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)

    query = session.query(State).filter(State.id == 2).one()
    query.name = "New Mexico"

    session.commit()


if __name__ == "__main__":
    alchemyFunction(sys.argv[1], sys.argv[2], sys.argv[3])
