import os
import pytest
from app import create_app
from app import db as _db


@pytest.fixture(scope='session')
def app(request):
    return create_app('config.TestingConfig')


@pytest.fixture(scope='module', autouse=True)
def app_context(app):
    """Creates a flask app context"""
    with app.app_context():
        yield app


@pytest.fixture
def client(app_context):
    return app_context.test_client(use_cookies=True)


@pytest.fixture(scope="module")
def db(app_context):

    _db.create_all()

    # # seed the database
    # seed_db()

    yield _db

    # teardown database
    # https://stackoverflow.com/a/18365654/5819113
    _db.session.remove()
    _db.drop_all()
    _db.get_engine(app_context).dispose()
    try:
        os.remove('tests/test.db')
    except FileNotFoundError:
        pass


# def seed_db():
#     # insert default users and roles
#     print("Seeding the database or something")


# ----------------------- OLD --------------------------------

# # create app for testing purpose - used by all tests
# @pytest.fixture(scope='module')
# def test_client(request):
#     app = create_app('config.TestingConfig')
#     with app.test_client() as test_client:
#         with app.app_context():
#             yield test_client


# # scope session: the fixture is destroyed at the end of the test session.
# @pytest.fixture(scope='module')
# def db(test_client):
#     """Session-wide test database."""
#     _db.create_all()
#     _db.app = test_client

#     yield _db

#     _db.drop_all()
#     try:
#         os.remove('tests/test.db')
#     except FileNotFoundError:
#         pass


# @pytest.fixture(scope='function')
# def session(db):
#     connection = db.engine.connect()
#     transaction = connection.begin()

#     options = dict(bind=connection)
#     session = db.create_scoped_session(options=options)

#     yield session

#     transaction.rollback()
#     connection.close()
#     session.remove()
