from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db(app):
    db.drop_all(app=app)
    db.create_all(app=app)
    db.session.commit()
