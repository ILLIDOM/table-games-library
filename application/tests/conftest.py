import os
import pytest
from core import create_app
from core import db as _db

# create app for testing purpose - used by all tests
@pytest.fixture(scope='session')
def test_client():
    app = create_app('config.TestingConfig')

    with app.test_client() as test_client:
        with app.app_context():
            yield test_client
    
    try:
        os.remove('tests/test.db')
    except FileNotFoundError:
        pass


# scope session: the fixture is destroyed at the end of the test session.
@pytest.fixture(scope='session')
def db(test_client):
    """Session-wide test database."""
    _db.create_all()
    _db.app = test_client
    yield _db
    _db.drop_all()


@pytest.fixture(scope='function')
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection)
    session = db.create_scoped_session(options=options)

    yield session

    # Finalize test here
    transaction.rollback()
    connection.close()
    session.remove()
