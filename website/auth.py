from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return ",<P>logout</P>"

@auth.route('/register')
def register():
    return ",<P>register</P>"
