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
    init_db()

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # blueprints
    from backend.views import bp, bp_api
    from backend.articles.views import bp_articles

    app.register_blueprint(bp)
    app.register_blueprint(bp_api)
    app.register_blueprint(bp_articles)

    return app
