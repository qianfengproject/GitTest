from flask_migrate import Migrate

from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def init_ext(app):
    Session(app=app)
    migrate.init_app(app=app, db=db)
    #session
    app.config['SECRET_KEY']='100'
    app.config['SESSION_TYPE']='redis'

    #sqlalchemy
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost:3306/GitTest'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app=app)

