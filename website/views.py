from flask import Blueprint, render_template
from flask_login import login_user, current_user, login_required, logout_user


views = Blueprint('views', __name__)


@views.route("/")
@login_required
def home():
    return render_template("index.html")

@views.route("/homepage")
@login_required
def homepage():
    return render_template("homepage.html")
