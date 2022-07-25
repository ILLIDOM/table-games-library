def test_valid_library_creation(client, db):
    response = client.post('/libraries', json={
        "name": "TestLibrary"
    })
    assert response.status_code == 201
    assert response.json["id"] == 1
    assert response.json["name"] == "TestLibrary"
    assert response.json["table-games"] == []


def test_invalid_library_creation_already_exists(client, db):
    library_name = "TestLibrary"
    response = client.post('/libraries', json={
        "name": "TestLibrary"
    })
    assert response.status_code == 400
    assert response.json["message"] == f"Library with name {library_name} already exists"