#!/usr/bin/python3
"""Module documentation """

from sqlalchemy import Column, Integer, String
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session, sessionmaker
import sys

Base = declarative_base()

if __name__ == "__main__":
    """ main function"""
    engine = create_engine('sqlite:///{}:{}@localhost:3306/{}'.format(
        sys.argv[3],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    for state in session().query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
