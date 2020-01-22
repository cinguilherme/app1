import os


class Config(object):
    """ Configuration object for the application """
    DEBUG = False
    CSRF_ENABLE = True
    SECRET = os.getenv('SECRET')
    SQL_ALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
    SQL_ALCHEMY_DATABASE_URI = 'postgressql://app1-postgres/test_db'
    DEBUG = True


class StagingConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
