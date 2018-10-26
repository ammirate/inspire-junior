from flask import abort, Blueprint, jsonify, request

from backend.articles.api import (
    get_articles,
    read_article,
    create_article,
)
from backend.articles.errors import ArticleMetadataError
from backend.articles.serializers import ArticleSchema


bp_articles = Blueprint('articles', __name__, url_prefix='/api/articles')


@bp_articles.route('/', methods=['GET'])
def get_articles_list():
    # curl -X GET http://0.0.0.0:5000/api/articles/1 -H "Content-Type: application/json"
    articles = get_articles()
    serialized = ArticleSchema(articles, many=True).data
    return jsonify(serialized)


@bp_articles.route('/<int:article_id>', methods=['GET'])
def get_article(article_id):
    article = read_article(article_id)

    if not article:
        abort(404, 'Article does not exists')

    serialized = ArticleSchema(article).data
    return jsonify(serialized)


@bp_articles.route('/', methods=['POST'])
def post_article():
    # curl -X POST http://0.0.0.0:5000/api/articles/ -d '{"title": "article 1", "category": "hep-th"}' -H "Content-Type: application/json"
    metadata = request.json

    try:
        article = create_article(metadata)
    except ArticleMetadataError as e:
        abort(400, e.message)

    serialized = ArticleSchema(article).data
    return jsonify(serialized)
