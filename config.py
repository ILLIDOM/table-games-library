class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'mykey'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@172.17.28.198:5432/table_game_library'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'mykey'

class TestingConfig(Config):
    TESTING = True