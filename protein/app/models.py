__author__ = 'dominic'

from app import db


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    menu = db.relationship('Food', backref='restaurant', lazy='dynamic')

    def __repr__(self):
        return '<Restaurant %r>' % (self.name)


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

    def __repr__(self):
        return '<Food %r>' % (self.name)