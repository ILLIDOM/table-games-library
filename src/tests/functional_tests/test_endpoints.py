from app.models.user_model import UserModel

def test_home_page(client):
    """
    
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"APP is running"


def test_user_schema_1(db):
    user = UserModel('domi', 'mypassword')
    
    db.session.add(user)
    db.session.commit()

    assert user.id == 1
    assert user.username == 'domi'

def test_user_schema_2(db):
    user = UserModel('timi', 'mypassword')
    
    db.session.add(user)
    db.session.commit()

    assert user.id == 2
    assert user.username == 'timi'