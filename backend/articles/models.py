from backend.db import db


class Article(db.Model):
    """Scientific article model"""
    id = db.Column(db.Integer, primary_key=True)
    abstract = db.Column(db.String(1000), nullable=True)
    category = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Article %d>' % self.id

    def dump(self):
        return dict(
            title=self.title,
            category=self.category,
            id=self.id,
            abstract=self.abstract
        )
