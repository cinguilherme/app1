from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

# to be defined
app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

from models.user import UserModel
from models.store import StoreModel
from models.item import ItemModel

if __name__ == '__main__':
    manager.run()

