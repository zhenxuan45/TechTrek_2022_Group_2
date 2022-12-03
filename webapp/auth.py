from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__) #usually the naming of blueprint follows the filename

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        #check user email is valid
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                #remember=True: rememebers user until flask session is cleared
                login_user(user, remember=True)
                flash('Logged in successfully', category='success')
                # return redirect(url_for('views.home'))
            else:
                flash('Incorrect Username or Password', category='error')
        else:
            flash('Incorrect Username or Password', category='error')
    
    return render_template("login.html", user=current_user)

@auth.route('/logout')
#this makes sure that logout cannot be accessed unless the user is logged in
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        #get all information from request.form using .get to get specific attributes
        username = request.form.get("username")
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        address = request.form.get("address")

        user = User.query.filter_by(username=username).first()
        if user:
            flash('User already exist, Please sign in', category='error')
        #validity check
        elif len(email) < 4:
            #flash error message
            #note that category can be any naming so long as you are able to recognize
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(username=username, email=email, last_name=last_name, first_name=first_name, address=address, password=generate_password_hash(password1, method='sha256'))
            #add new_user to db
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html", user=current_user)