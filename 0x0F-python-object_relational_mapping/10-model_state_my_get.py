#!/usr/bin/python3
"""
prints the State object with the name
passed as argument from the databasehbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    access database codesource
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state is not None:
        print('{0}'.format(state.id))
    else:
        print("Not found")
