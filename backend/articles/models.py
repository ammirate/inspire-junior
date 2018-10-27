from backend.db import db
from backend.categories.models import Category


class Article(db.Model):
    """Scientific article model"""
    id = db.Column(db.Integer, primary_key=True)
    abstract = db.Column(db.String(1000), nullable=True)
    title = db.Column(db.String(200), nullable=False)

    category_id = db.Column(
        db.Integer,
        db.ForeignKey(Category.id),
        nullable=True
    )

    category = db.relationship(Category, backref='articles', uselist=False)

    def __repr__(self):
        return '<Article %d>' % self.id

    def dump(self):
        return dict(
            category={} if not self.category else self.category.dump(),
            abstract=self.abstract,
            category_id=self.category_id,
            id=self.id,
            title=self.title,
        )
