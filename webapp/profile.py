import os
from re import T
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime
from datetime import date
import json
from flask import Blueprint
from . import db
from .models import User

profile=Blueprint("profile",__name__)

CORS(profile)

@profile.route("/user/<int:userid>")
def user_by_id(userid):
    user = User.query.filter_by(userid=userid).first()
    if user:
        return jsonify({
            "data": user.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Person not found."
        }), 404

@profile.route("/user_create", methods=['POST'])
def create_user():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('userid', 'username', 'password', 'first_name',
                       'last_name','email', 'address','OptIntoPhyStatements')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    user = User(**data)
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500
