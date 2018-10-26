import pytest

from backend.db import db
from backend.factory import create_app
from backend.articles.models import Article


@pytest.fixture
def test_app():
    test_app = create_app('testing')
    return test_app


@pytest.fixture
def test_client(test_app):
    with test_app.test_client() as client:
        return client


@pytest.fixture
def article():
    return Article(
        title='A Model of Leptons',
        category='hep-th',
        abstract='lorem ipsum'
    )


@pytest.fixture
def db_article(test_app, article):
    db.session.add(article)
    db.session.commit()
    yield article
    db.session.query(Article).filter_by(id=article.id).delete()
    db.session.commit()
