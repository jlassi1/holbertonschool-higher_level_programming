#!/usr/bin/python3
"""Module documentation """

from sys import argv
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """ main function"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).order_by(
                  State.id).filter(State.name(argv[4]))
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
    session.close()
