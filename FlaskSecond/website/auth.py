from flask import Blueprint , render_template, request , flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db    
from flask_login import login_user, login_required, logout_user, current_user

auth=Blueprint("auth",__name__)

@auth.route('/login', methods=['POST','GET'])
def login(): 
    if request.method == 'POST': 
        email=request.form.get('email')
        emailing=User.query.all()
        for emails in emailing: 
            print(emails.email)
            print(emails.id)
        password = request.form.get('password')
        user=User.query.filter_by(email=email).first()
        if user: 
            if check_password_hash(user.password,password): 
                flash('Log In Successful', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else: 
                flash('Wrong Password', category='error') 
        else: 
            flash('No such USER', category='error') 
        
    # data=request.form.get('email')
    # print(data)
    return render_template('login.html', user=current_user)


@auth.route('/logout') 
@login_required
def logout(): 
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET','POST'])
def sign_up(): 
    if request.method=="POST": 
        email = request.form.get('email') 
        first_name=request.form.get('firstName')
        last_name=request.form.get('lastName')
        username = request.form.get('username')
        address = request.form.get('address')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        optout = request.form.get('optout')
        user=User.query.filter_by(email=email).first()
        
        if user: 
            flash('user exist liao', category='error')
            return 'user created'
        elif len(email) < 4: 
            flash('email too short',category='error')
            return 'email too short'
        elif len(first_name) < 2: 
            flash('first name too short',category='error')
            return 'first name too short bro'
        elif password1!=password2: 
            flash('passwords not the same', category='error')
        elif len(password1) < 7: 
            flash('passwords not long enough', category='error')
        else: 
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1,method='sha256'),
                address=address, username=username, optphy=(optout=="true"))
            # print(new_user.email)
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created', category="SUCCESS")
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
    return  render_template('sign_up.html', user=current_user)