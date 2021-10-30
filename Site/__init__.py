from flask import Flask
from datetime import timedelta

app = Flask(__name__)

app.config['SECRET_KEY'] = ""
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=31)

def create_app():
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .admin import admin
    app.register_blueprint(admin, url_prefix='/')

    from data import create_db
    create_db(app)

    return app

from data.models import ListofUsers

class User:
    def __init__(self):
        self.uid = None

    def data(self):
        return ListofUsers.query.filter_by(Username = self.uid).first()

    def isLogin(self):
        if self.uid != None:
            return True
        else:
            return False