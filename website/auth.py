from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, current_user, login_required, logout_user, UserMixin

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        emailL = request.form.get('email')
        passwordL = request.form.get('password')
        user = User.query.filter_by(email=emailL).first()
        if user:
            if check_password_hash(user.password, passwordL):
                flash("Logged in successfully!", category='success!')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Wrong password!", category='error!')
        else:
            flash("Email didn't exist.", category="error!")
    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return  redirect(url_for("auth.login"))

@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == "POST":
        emailR = request.form.get('email')
        UsernameR = request.form.get('Username')
        password1R = request.form.get('password1')
        password2R = request.form.get('password2')

        user = User.query.filter_by(email=emailR).first()
        if user:
            flash("Email already exists.", category="error!")
        elif len(emailR) < 3:
            flash('Email must be 2 or more characters.', category="error!")
        elif len(UsernameR) < 2:
            flash('first name must be more than 1 characters.', category="error!")
        elif password1R != password2R:
            flash('Passwords did not matced.', category="error!")
        elif len(password1R) < 8:
            flash('Password characters must be 8 or more.', category="error!")
        else:
            #create new user and add it to data base after encrepted
            new_user = User(email=emailR,Username=UsernameR,password=generate_password_hash(password1R, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created successfuly!!.', category="success!")
            return redirect(url_for('views.home'))
    return render_template("register.html")
