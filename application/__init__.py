from flask import Flask, redirect, url_for, session, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, pprint
from flask_migrate import Migrate
from flask_restful import Api
import os

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
api = Api


def create_app(mode='prod'):

    app = Flask(__name__)

    from application.config import config_name
    app.config.from_object(config_name[mode])

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from application.views.travel_info import travel_info_bp
    app.register_blueprint(travel_info_bp)

    @app.route('/', host="travel_info.com:5000")
    def init():
        return "Hello World"

    @app.route('/main')
    def main():
        return "this is main page"

    return app



