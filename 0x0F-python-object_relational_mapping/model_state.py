#!/usr/bin/python3

''' import sqlachemy for ORM '''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ class to model our table in the database """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
