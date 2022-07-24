from core.models.user_model import UserModel

def test_home_page(test_client):
    """
    
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"APP is running"


def test_user_schema_1(session):
    user = UserModel('domi', 'mypassword')
    
    session.add(user)
    session.commit()

    assert user.id == 1
    assert user.username == 'domi'

def test_user_schema_2(session):
    user = UserModel('timi', 'mypassword')
    
    session.add(user)
    session.commit()

    assert user.id == 2
    assert user.username == 'timi'