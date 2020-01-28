import os

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

# the values of those depend on your setup

local_bd = 'postgresql+psycopg2://postgres:Postgres2019!@app1postgres:5432/test'
try:
    DB_URL = os.environ['DATABASE_URL']
except:
    DB_URL = local_bd

DATABASE_URL = DB_URL

def get_postgres_uri():
    return DATABASE_URL