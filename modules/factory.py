from flask_cors import CORS
from flask import Flask
from config import config
from modules.db_model import db
from modules.feed.feed_controller import feed_api

def create_app(app_name, config_name):
    app = Flask(app_name, static_url_path='')
    app.config.from_object(config[config_name])
    CORS(app)
    init_db(app)
    register_blueprints(app)
    with app.app_context():
        app.db.create_all()
    return app

def register_blueprints(app):
    app.register_blueprint(feed_api)
    # all blueprints (Controllers) should be imported and assigned to the global flask app here
    pass

def init_db(app):
    db.init_app(app)
    app.db = db
    # from modules.models.feedings import Feedings
