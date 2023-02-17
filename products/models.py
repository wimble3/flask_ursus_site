import sqlite3
from flask import abort
from app import db


class Knife(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35), nullable=False)
    slug = db.Column(db.String(50), unique=True, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    blade_material = db.Column(db.String(50), nullable=False)
    blade_length = db.Column(db.Integer, nullable=False)
    blade_thickness = db.Column(db.Integer, nullable=False)
    handle_material = db.Column(db.Integer, nullable=False)
    coating = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(250), unique=True, nullable=False)

    def __repr__(self):
        return f'Knife {self.name}'


def get_knifes():
    try:
        return Knife.query.all()
    except sqlite3.DatabaseError:
        abort(500)


def get_knife_by_path(path):
    knife = None
    try:
        return Knife.query.filter(Knife.slug.like(f'{path}')).first()
    except sqlite3.DatabaseError:
        abort(500)

    if not knife:
        abort(404)

    return knife
