# third-party imports
from flask import Flask, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI, status, exceptions
import json

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

from flask_migrate import Migrate


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    migrate = Migrate(app, db)

    from app.models import Company

    @app.route('/v1/mail/ingest', methods=['POST'])
    def ingest_mail():
        print('Successful post: ', request.data)
        return json.dumps({'success': True}), status.HTTP_200_OK, {'ContentType': 'application/json'}

    @app.route('/v1/mail/ingest-errors', methods=['POST'])
    def ingest_mail_errors():
        print('Failed post: ', request.data)
        return json.dumps({'success': False}), status.HTTP_500_INTERNAL_SERVER_ERROR, {'ContentType': 'application/json'}

    return app
