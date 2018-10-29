from __future__ import absolute_import, division, print_function

from flask import Blueprint, jsonify


bp_api = Blueprint('api', __name__, url_prefix='/api')
bp = Blueprint('blueprint', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def home():
    return "This is my Scraper App"


@bp_api.route('/', methods=['GET'])
def api():
    return jsonify(success=True, status_code=200)


@bp_api.route('/test', methods=['GET'])
def test():
    import os
    import requests

    try:
        scraper_url = "http://{}:{}".format(
            os.environ['SCRAPER_SITE_1_PORT_5000_TCP_ADDR'],
            os.environ['SCRAPER_SITE_PORT_5000_TCP_PORT'],
        )
    except KeyError:
        scraper_url = "http://0.0.0.0:8080"

    resp = requests.get(scraper_url).text
    envs = {k: v for (k, v) in os.environ.items()}

    resp = {'scraper': resp, 'env': envs}
    return jsonify(resp)
