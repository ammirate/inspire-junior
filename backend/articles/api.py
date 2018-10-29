from __future__ import absolute_import, division, print_function

from backend.db import db
from backend.articles.models import Article
from backend.articles.errors import ArticleMetadataError

from backend.categories.api import read_category_by_name, create_category


def _extract_data_from_json(json_model):
    metadata = dict(
        category_id=json_model.get('category_id'),
        title=json_model['title'],
        abstract=json_model.get('abstract'),
    )
    return metadata


def _check_data(json_model, smart=False):
    if not isinstance(json_model, dict):
        raise TypeError('Dict expected, got ' + str(type(json_model)))
    if 'title' not in json_model:
        raise ArticleMetadataError(
            '`Title` is a required field. Got {}'.format(
                json_model)
        )
    if smart:
        if 'category' not in json_model:
            raise ArticleMetadataError(
                '`category` is a required field. Got {}'.format(
                    json_model)
            )
    else:
        if 'category_id' not in json_model:
            raise ArticleMetadataError(
                '`category_id` is a required field. Got {}'.format(
                    json_model)
            )


def create_article(json_model):
    """Add an Article in the DB

    Args:
        json_model(Dict): the Article metadata to insert in the DB

    Return:
        (Article): the model just created

    Raise:
        ArticleMetadataError if the metadata is not compliant with the model
    """
    _check_data(json_model)
    metadata = _extract_data_from_json(json_model)
    article = Article(**metadata)
    db.session.add(article)
    db.session.commit()
    return article


def smart_create_article(json_model):
    """Add an Article in the DB and the related category if it does not exist

    Args:
        json_model(Dict): the Article metadata to insert in the DB

    Return:
        (Article): the model just created

    Raise:
        ArticleMetadataError if the metadata is not compliant with the model
    """
    _check_data(json_model, smart=True)
    metadata = _extract_data_from_json(json_model)

    cat_name = json_model['category']
    category = read_category_by_name(cat_name)
    if not category:
        category = create_category(cat_name)

    metadata['category_id'] = category.id
    article = Article(**metadata)
    db.session.add(article)
    db.session.commit()
    return article


def read_article(article_id):
    """Add an Article in the DB

    Args:
        article_id(Int): the Article ID

    Return:
        (Article): the Article requested or None
    """
    article = db.session.query(Article).get(article_id)
    return article


def get_articles():
    """Return all the Articles from the DB

    Return:
        (List): the Articles in the DB
    """
    return db.session.query(Article).all()


def get_articles_by_category(category_id):
    """Return all the Articles belonging to the given category

    Args:
        category_id(Int): Category ID

    Return:
        (List): the Articles in the DB
    """
    return db.session.query(Article).filter_by(category_id=category_id).all()


def update_article(article_id, json_model):
    """Update an Article in the DB

    Args:
        json_model(Dict): the Article metadata to update in the DB

    Return:
        (Int): ID of the updated Article

    Raise:
        ArticleMetadataError if the metadata is not compliant with the model
    """
    _check_data(json_model)
    new_data = _extract_data_from_json(json_model)
    ret_val = db.session.query(Article).filter_by(id=article_id).update(new_data)
    db.session.commit()
    return ret_val


def delete_article(article_id):
    """Delete an Article from the DB

    Args:
        article_id(Int): the Article's ID

    Return:
        (Int): ID of the article deleted

    """
    return_val = db.session.query(Article).filter_by(id=article_id).delete()
    db.session.commit()
    return return_val
