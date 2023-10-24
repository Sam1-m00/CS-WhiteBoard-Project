from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return ",<P>login</P>"

@auth.route('/logout')
def logout():
    return ",<P>logout</P>"

@auth.route('/register')
def register():
    return ",<P>register</P>"
