from __future__ import absolute_import, division, print_function

from backend.db import db


class Category(db.Model):
    """Scientific category model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return '<Category %d>' % self.id

    def dump(self):
        return dict(
            id=self.id,
            name=self.name,
        )
