from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URL
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI']= DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'whocares'
app.config['SESSION_TYPE'] = 'filesystem'


moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()