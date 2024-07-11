import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

@pytest.fixture(scope='session')
def db():
    engine = create_engine('sqlite:///{}'.format(os.path.join(os.path.dirname(__file__), 'test.db')))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
