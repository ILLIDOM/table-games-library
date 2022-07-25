from app.models.user_model import UserModel
from app.models.table_game_model import TableGameModel

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the username and password are correct
    """
    user = UserModel('domi', 'mypassword')
    assert user.username == 'domi'
    assert user.password == 'mypassword'

def test_new_table_game():
    """
    """
    game = TableGameModel('7 Wonders', 'Family', 1, 1)
    assert game.name == "7 Wonders"
    assert game.type == 'Family'
    assert game.user_id == 1
    assert game.library_id == 1