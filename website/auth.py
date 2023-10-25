from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return  "<p>Logout</p>"

@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 3:
            flash('Email must be 2 or more characters.', category="error!")
        elif len(firstName) < 2:
            flash('first name must be more than 1 characters.', category="error!")
        elif password1 != password2:
            flash('Passwords did not matced.', category="error!")
        elif len(password1) < 8:
            flash('Password characters must be 8 or more.', category="error!")
        else:
            flash('Account created successfuly!!.', category="success!")

    return render_template("register.html")
