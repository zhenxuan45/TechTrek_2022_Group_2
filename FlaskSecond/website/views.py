from flask import Blueprint , render_template, request, flash, jsonify
from flask_login import  login_required, current_user
from .models import User, Transaction
from sqlalchemy.inspection import inspect
from . import db
import json

views=Blueprint("views",__name__)


@views.route('/',methods=['POST','GET'])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")
        delete = request.form.get("delete")
        if note != None:
            if len(note) < 1:
                flash("Nothing written...", category="error")
            else:
                new_note = Transaction(data=note, user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                flash("Note added!", category="success")
        elif delete != None:
            delete = int(delete)
            if delete == current_user.id:
                noteID = request.form.get("todelete")
                noteID = int(noteID)
                noted = Transaction.query.get(noteID)
                if noted:    
                    db.session.delete(noted)
                    db.session.commit()
                    flash("Note deleted", category="success")

    return render_template("home.html", user=current_user)

    
@views.route('/profile',methods=['POST','GET'])
@login_required
def profile():
    if request.method=="POST":
        newemail = request.form.get("email")
        changeUser = User.query.get(current_user.id)
        changeUser.address = request.form.get("address")
        changeUser.email = newemail
        db.session.commit()
    return render_template("profile.html", user=current_user)

@views.route('/transactions',methods=['POST','GET'])
@login_required
def transactions():
    return render_template("transactions.html", user=current_user)