from flask import Blueprint, jsonify

from backend.modules.articles.api import (
    create_article,
    delete_article,
    get_articles,
    read_article,
    update_article,
)
from backend.modules.articles.serializer import ArticleSerializer


bp_articles = Blueprint('articles', __name__, url_prefix='/api/articles')


@bp_articles.route('/', methods=['GET'])
def get_articles_list():
    articles = get_articles()
    serialized = ArticleSerializer(articles, many=True).data
    return jsonify(serialized)


@bp_articles.route('/<int:article_id>', methods=['GET'])
def get_article(article_id):
    article = read_article(article_id)
    serialized = ArticleSerializer(article).data
    return jsonify(serialized)
