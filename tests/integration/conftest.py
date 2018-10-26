import pytest

from backend.db import db
from backend.factory import create_app
from backend.articles.models import Article
from backend.categories.models import Category


@pytest.fixture
def test_app():
    test_app = create_app('testing')
    return test_app


@pytest.fixture
def test_client(test_app):
    with test_app.test_client() as client:
        return client


@pytest.fixture
def db_category(test_app):
    category = Category(name='hep-th')
    db.session.add(category)
    db.session.commit()
    yield category
    db.session.query(Article).filter_by(id=category.id).delete()
    db.session.commit()


@pytest.fixture
def article(db_category):
    return Article(
        title='A Model of Leptons',
        category_id=db_category.id,
        abstract='lorem ipsum'
    )


@pytest.fixture
def db_article(test_app, article):
    db.session.add(article)
    db.session.commit()
    yield article
    db.session.query(Article).filter_by(id=article.id).delete()
    db.session.commit()


@pytest.fixture
def db_category(test_app):
    category = Category(name='hep-th')
    db.session.add(category)
    db.session.commit()
    yield category
    db.session.query(Category).filter_by(id=category.id).delete()
    db.session.commit()
