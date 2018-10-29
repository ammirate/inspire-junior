from __future__ import absolute_import, division, print_function

from flask import abort, Blueprint, jsonify, request

from backend.articles.api import (
    get_articles,
    get_articles_by_category,
    read_article,
    create_article,
    smart_create_article,
)
from backend.articles.errors import ArticleMetadataError
from backend.articles.serializers import ArticleSchema


bp_articles = Blueprint('articles', __name__, url_prefix='/api/articles')


@bp_articles.route('/', methods=['GET'])
def get_articles_list():
    category_id = request.args.get('category_id')

    try:
        category_id = int(category_id)
    except (ValueError, TypeError):
        category_id = None

    if category_id and category_id >= 0:
        articles = get_articles_by_category(category_id)
    else:
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
    metadata = request.json
    smart_flag = request.args.get('smart')

    try:
        if smart_flag:
            article = smart_create_article(metadata)
        else:
            article = create_article(metadata)

    except ArticleMetadataError as e:
        abort(400, e.message)

    serialized = ArticleSchema(article).data
    return jsonify(serialized)
