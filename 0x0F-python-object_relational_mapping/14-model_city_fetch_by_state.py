#!/usr/bin/python3
"""Module documentation """

from sys import argv
from sqlalchemy import create_engine
from model_state import State, Base
from model_city import City
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """ main function"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for st, ct in session.query(State, City).order_by(City.id)
    .filter(State.id == City.state_id).all():
        print("{}: ({}) {}".format(st.name, st.id, ct.name))
    session.close()
