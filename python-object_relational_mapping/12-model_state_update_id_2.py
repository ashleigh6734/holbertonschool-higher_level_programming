#!/usr/bin/python3
"""
Task 12: Update State name where id = 2
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

    # Fetch state with id = 2 and update its name
    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
