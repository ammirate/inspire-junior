from flask import Blueprint, jsonify


bp_api = Blueprint('api', __name__, url_prefix='/api')
bp = Blueprint('blueprint', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def home():
    return "This is my Scraper App"


@bp_api.route('/', methods=['GET'])
def api():
    return jsonify(success=True, status_code=200)

