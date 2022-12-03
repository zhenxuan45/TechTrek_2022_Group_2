from flask import Blueprint , render_template, request, flash, jsonify
from flask_login import  login_required, current_user
from .models import User
from sqlalchemy.inspection import inspect
from . import db
import json

views=Blueprint("views",__name__)


@views.route('/',methods=['POST','GET'])
@login_required
def home():
    if request.method == 'POST': 
        data=request.form.get('note')
        if len(data)<1: 
            flash("TOO SHORT", category='error')
        else:
            new_note = Note(data=data, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("NOTE ADDED", category='success')
            notes=Note.query.all()
            print(current_user.notes)
            for note in notes:
                print(note.id)
                print(note.data)
            
            # print(Note.query.filter_by(data='mark'))
    return render_template('home.html',user=current_user)

    
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data) 
    noteId  = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit() 
            flash("DELETED", category='success')
            return jsonify({})
    return jsonify({})
    
