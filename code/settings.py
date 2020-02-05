import os

MONGO_URI = os.environ.get('MONGO_URL')
POSTGRES_URL = os.environ.get('DATABASE_URL')
SECRET = os.environ.get('SECRET')
SCHEMA = os.environ.get('POSTGRES_SCHEMA')
