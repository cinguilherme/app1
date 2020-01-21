
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ
from sqlalchemy.ext.declarative import declarative_base
from models.user import UserModel 

Base = declarative_base()

def get_env_variable(name):
    try:
        return environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

# the values of those depend on your setup
POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
# Create engine

engine = create_engine(DB_URL, echo=True)

