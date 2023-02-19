import sqlite3
from flask import abort
from app import db


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35), nullable=False)
    slug = db.Column(db.String(55), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.name} - {self.slug}'


def get_menu_items():
    try:
        return MenuItem.query.all()
    except sqlite3.OperationalError:
        abort(500)
