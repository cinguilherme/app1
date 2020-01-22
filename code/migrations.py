from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, create_engine
import postgres
from models.user import UserModel
from models.item import ItemModel

postgres_uri = postgres.get_postgres_uri()

def create_user_table():

    print(__name__)
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = postgres_uri
    
    create_engine(postgres_uri, echo=True)

    _db = SQLAlchemy()
    _db.init_app(app)
    _db.create_all()
    _db.session.commit()
    print('did this run?')

    meta = MetaData()


create_user_table()