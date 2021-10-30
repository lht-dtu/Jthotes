from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

def create_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .models import ListofUsers

    if not path.exists("../data/data.db"):
        db.create_all(app=app)
