def test_valid_register(client, db):
    response = client.post('/register', json={
        "username": "Hans",
        "password": "mypassword"
    })
    assert response.status_code == 201
    assert response.json["message"] == 'User created successfully.'


def test_invalid_register_user_already_exists(client, db):
    response = client.post('/register', json={
        "username": "Hans",
        "password": "mypassword"
    })
    assert response.status_code == 400
    assert response.json["message"] == 'A user with that username already exists'


def test_valid_login(client, db):
    response = client.post('/login', json={
        "username": "Hans",
        "password": "mypassword"
    })
    assert response.status_code == 200
    assert response.json["access_token"] != ""
    assert response.json["refresh_token"] != ""


def test_invalid_login_non_existent_user(client, db):
    response = client.post('/login', json={
        "username": "hahah",
        "password": " "
    })
    assert response.status_code == 401
    assert response.json["message"] == "invalid credentials"


def test_invalid_login_wrong_password(client, db):
    response = client.post('/login', json={
        "username": "Hans",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.json["message"] == "invalid credentials"
