def test_register(test_client):
    response = test_client.post('/register', json={
        "username": "Hans",
        "password": "mypassword"
    })
    assert response.status_code == 201
    assert response.json["message"] == 'User created successfully.'