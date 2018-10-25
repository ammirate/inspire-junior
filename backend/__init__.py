from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from backend.views import bp_api


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
db = SQLAlchemy(app)


from backend.modules.articles.views import bp_articles


app.register_blueprint(bp_api)
app.register_blueprint(bp_articles)


@app.route('/', methods=['GET'])
def home():
    return 'backend app'



# TODO
# 404 in the views when not model isinstance() found
# error handling for api
# flask login + UI