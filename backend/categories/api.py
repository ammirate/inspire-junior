from backend.db import db
from backend.categories.models import Category
from backend.categories.errors import CategoryValueError


def create_category(name):
    """Add an Category in the DB

    Args:
        json_model(Dict): the Category metadata to insert in the DB

    Return:
        (Category): the model just created

    Raise:
        CategoryMetadataError if the metadata is not compliant with the model
    """
    if not name:
        raise CategoryValueError()

    cat = Category(name=name)
    db.session.add(cat)
    db.session.commit()
    return cat


def read_category(cat_id):
    """Add a Category in the DB

    Args:
        cat_id(Int): the Category ID

    Return:
        (Category): the Category requested or None
    """
    article = db.session.query(Category).get(cat_id)
    return article


def get_categories():
    """Return all the Categories from the DB

    Return:
        (List): the Categories in the DB
    """
    return db.session.query(Category).all()


def update_category(article_id, name):
    raise NotImplementedError


def delete_category(article_id):
    """Delete a Category from the DB

    Args:
        article_id(Int): the Category's ID

    Return:
        (Int): ID of the article deleted
    """
    return_val = db.session.query(Category).filter_by(id=article_id).delete()
    db.session.commit()
    return return_val


def delete_category_by_name(cat_name):
    """Delete a Category from the DB

    Args:
        article_id(Int): the Category's ID

    Return:
        (Int): ID of the article deleted
    """
    return_val = db.session.query(Category).filter_by(name=cat_name).delete()
    db.session.commit()
    return return_val


