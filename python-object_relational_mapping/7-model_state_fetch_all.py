#!/usr/bin/python3
"""
Task 7: List all State objects from hbtn_0e_6_usa using SQLAlchemy
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine and bind session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects sorted by id
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")

    session.close()
