from flask import Blueprint, render_template, redirect

auth = Blueprint('auth', __name__)

from . import User
current_user = User()

@auth.route("/begin", methods = ['GET', 'POST'])
def begin():
    if current_user.uid:
        return redirect("/")
    return render_template("begin.html")

@auth.route("/end")
def end():
    if current_user.isLogin():
        current_user.uid = None
    return redirect("/")