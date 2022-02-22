import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'mykey'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@172.21.226.227:5432/table_game_library' # use IP of WSL
    #SQLALCHEMY_DATABASE_URI = f"postgresql://{ os.getenv('POSTGRE_USER') }:{ os.getenv('POSTGRE_PASSWORD') }@{ os.getenv('POSTGRE_CONNECTION') }/{ os.getenv('POSTGRE_DB') }"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'mykey'

class TestingConfig(Config):
    TESTING = True