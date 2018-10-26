import json
import pytest
import pkg_resources

from backend.db import db
from backend.articles.api import (
    get_articles,
    read_article,
    create_article,
    update_article,
    delete_article,
)
from backend.articles.models import Article
from backend.articles.errors import ArticleMetadataError


@pytest.fixture
def article():
    return Article(
        title='A Model of Leptons',
        category='hep-th',
        abstract='lorem ipsum'
    )


@pytest.fixture
def db_article(article):
    db.session.add(article)
    db.session.commit()
    yield article
    db.session.query(Article).filter_by(id=article.id).delete()
    db.session.commit()


def test_get_articles_empty_db(test_app):
    assert get_articles() == []


def test_get_articles_non_empty_db(test_app, db_article):
    assert len(get_articles()) == 1


def test_read_article(test_app, db_article):
    article = read_article(db_article.id)
    assert article
    assert article.title == 'A Model of Leptons'
    assert article.category == 'hep-th'
    assert article.abstract == 'lorem ipsum'


def test_read_article_not_in_db(test_app):
    read_article(98877554)


def test_create_article_no_abstract(test_app):
    metadata = {
        'title':    'A Model of Leptons',
        'category': 'hep-ex',
    }
    model = create_article(metadata)
    model_id = model.id

    db_model = read_article(model_id)
    assert db_model.title == metadata['title']
    assert db_model.category == metadata['category']
    assert db_model.abstract is None


def test_create_article_long_abstract(test_app):
    metadata_path = pkg_resources.resource_filename(
        __name__,
        'fixtures/too_long_abstract.json'
    )
    metadata = json.load(open(metadata_path))

    model = create_article(metadata)
    model_id = model.id

    db_model = read_article(model_id)
    assert db_model.title == metadata['title']
    assert db_model.category == metadata['category']
    assert db_model.abstract == metadata['abstract']


def test_create_article_no_category_raises_error(test_app):
    metadata = {
        'title': 'A Model of Leptons',
    }

    with pytest.raises(ArticleMetadataError):
        create_article(metadata)


def test_create_article_no_title_raises_error(test_app):
    metadata = {
        'category': 'hep-tx',
    }

    with pytest.raises(ArticleMetadataError):
        create_article(metadata)


def test_update_article(test_app, db_article):
    metadata = db_article.dump()
    metadata['title'] = 'Updated title'
    updated_id = update_article(db_article.id, metadata)

    updated_article = read_article(updated_id)
    assert updated_article.title == 'Updated title'


def test_delete_article(test_app, db_article):
    article_id = db_article.id
    delete_article(article_id)
    assert read_article(article_id) is None
