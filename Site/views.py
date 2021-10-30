from flask import Blueprint, render_template, redirect, request

views = Blueprint('views', __name__)

from .auth import current_user

@views.route("/", methods = ['GET', 'POST'])
def index():
    if current_user.isLogin():
        if request.method == 'POST':
            pass
        else:
            return render_template("index.html", user = current_user)
    else:
        return "You didn't Login!"

@views.route("/<s>")
def other(s):
    return redirect("/")