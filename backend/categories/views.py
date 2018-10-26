import json
from flask import abort, Blueprint, jsonify, request

from backend.categories.api import (
    get_categories,
    read_category,
    create_category,
)
from backend.categories.errors import CategoryValueError
from backend.categories.serializers import CategorySchema


bp_categories = Blueprint('categories', __name__, url_prefix='/api/categories')


@bp_categories.route('/', methods=['GET'])
def get_categories_list():
    categories = get_categories()
    serialized = CategorySchema(categories, many=True).data
    return jsonify(serialized)


@bp_categories.route('/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = read_category(category_id)

    if not category:
        abort(404, 'Article does not exists')

    serialized = CategorySchema(category).data
    return jsonify(serialized)


@bp_categories.route('/', methods=['POST'])
def post_category():
    metadata = json.loads(request.data)

    try:
        category = create_category(metadata.get('name'))
    except CategoryValueError as e:
        abort(400, e.message)

    serialized = CategorySchema(category).data
    return jsonify(serialized)
