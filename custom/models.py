import sqlite3
from flask import abort
from app import db


class CustomOrder(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    payment_number = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    length = db.Column(db.Integer, db.ForeignKey('length_price.value'), nullable=False)
    blade_material = db.Column(db.Integer, db.ForeignKey('blade_material_price.value'), nullable=False)
    blade_length = db.Column(db.Integer, db.ForeignKey('blade_length_price.value'), nullable=False)
    blade_thickness = db.Column(db.Integer, db.ForeignKey('blade_thickness_price.value'), nullable=False)
    handle_material = db.Column(db.Integer, db.ForeignKey('handle_material_price.value'), nullable=False)
    coating = db.Column(db.Integer, db.ForeignKey('coating_price.value'), nullable=False)


class Price:
    value = db.Column(db.String, primary_key=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.value}'


def get_prices(cls):
    try:
        return cls.query.all()
    except sqlite3.OperationalError:
        abort(500)


def get_price_by_value(cls, value):
    try:
        return cls.query.filter(cls.value.like(f'{value}')).first()
    except sqlite3.OperationalError:
        abort(500)


def add_custom_order(**kwargs):
    try:
        custom_order = CustomOrder(**kwargs)
        db.session.add(custom_order)
        db.session.commit()
    except sqlite3.OperationalError:
        abort(500)


class LengthPrice(Price, db.Model): pass


class BladeMaterialPrice(Price, db.Model): pass


class BladeLengthPrice(Price, db.Model): pass


class BladeThicknessPrice(Price, db.Model): pass


class HandleMaterialPrice(Price, db.Model): pass


class CoatingPrice(Price, db.Model): pass
