import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'mykey'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@postgres:5432/table_game_library' # use IP of WSL
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@172.21.226.227:5432/table_game_library' # use IP of WSL
    SQLALCHEMY_DATABASE_URI = f"postgresql://{ os.getenv('POSTGRES_USER') }:{ os.getenv('POSTGRES_PASSWORD') }@{ os.getenv('POSTGRES_CONNECTION') }/{ os.getenv('POSTGRES_DB') }"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'mykey'

class TestingConfig(Config):
    TESTING = True