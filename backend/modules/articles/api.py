from backend import db
from backend.modules.articles.models import Article


def _extract_data_from_json(json_model):
    metadata = dict(
        category=json_model['category'],
        title=json_model['title'],
        abstract=json_model.get('abstract'),
    )
    return metadata


def create_article(json_model):
    article = _extract_data_from_json(json_model)
    db.session.add(article)
    db.session.commit()
    return article


def read_article(article_id):
    article = db.session.query(Article).get(article_id)
    return article


def get_articles():
    return db.session.query(Article).all()


def update_article(article_id, json_model):
    new_data = _extract_data_from_json(json_model)
    ret_val = db.session.query(Article).filter_by(id=article_id).update(new_data)
    db.session.commit()
    return ret_val


def delete_article(article_id):
    return_val = db.session.query(Article).filter_by(id=article_id).delete()
    db.session.commit()
    return return_val
