import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'mykey'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@postgres:5432/table_game_library' # use IP of WSL
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@172.17.185.48:5432/table_game_library' # use IP of WSL
    #SQLALCHEMY_DATABASE_URI = f"postgresql://{ os.getenv('POSTGRES_USER') }:{ os.getenv('POSTGRES_PASSWORD') }@{ os.getenv('POSTGRES_CONNECTION') }/{ os.getenv('POSTGRES_DB') }"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tests/test.db'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'mykey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../tests/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'mykey'