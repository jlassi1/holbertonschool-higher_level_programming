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
    loui = State(name="Louisiana")
    session.add(loui)
    session.rollback()
    print("{}".format(loui.id))
    session.close()
