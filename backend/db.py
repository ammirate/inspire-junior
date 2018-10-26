from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
