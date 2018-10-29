from __future__ import absolute_import, division, print_function

from flask import Flask
from flask_cors import CORS

from config import CONFIGS
from backend.db import db, init_db


def create_app(config_env):

    print (config_env)

    app = Flask(__name__)
    app.config.from_object(CONFIGS[config_env])
    app.app_context().push()

    # extensions
    db.init_app(app)
    init_db(app)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # blueprints
    app.url_map.strict_slashes = False

    from backend.views import bp, bp_api
    from backend.articles.views import bp_articles
    from backend.categories.views import bp_categories

    app.register_blueprint(bp)
    app.register_blueprint(bp_api)
    app.register_blueprint(bp_articles)
    app.register_blueprint(bp_categories)

    return app
