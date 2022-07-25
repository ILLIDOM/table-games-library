def test_valid_table_game_creation(client, db):
    # TODO - get jwt and send it
    response = client.post('/table-games', json={
        "name": "7 Wonders",
        "type": "Family",
        "library_id": 1
    })
    assert response.status_code == 201
    assert response.json["id"] == 1
    assert response.json["name"] == "TestLibrary"
    assert response.json["type"] == []
    assert response.json["user_id"] == []
    assert response.json["library_id"] == []
