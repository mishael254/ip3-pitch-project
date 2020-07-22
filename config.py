import os

class Config:
    '''
    General configuration parent class
    '''
    
    SECRET_KEY ='127'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")




class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    ''' 

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://foxx:1234@localhost/pitch_test'   
     
    


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://foxx:1234@localhost/pitch'

    DEBUG = True

config_options = {
    'development' :DevConfig,
    'production' :ProdConfig,
    'test':TestConfig
}    