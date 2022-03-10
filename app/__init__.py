import logging
from logging.handlers import RotatingFileHandler
import datetime

import os

from config import Config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
from app.models import *

db.create_all()

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/%s_espp_mock.log' % datetime.datetime.utcnow().strftime('%Y%m%d'),
                                       encoding='utf8', maxBytes=10240000, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s')
    )
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('espp_mock startup')

    werkzeug_log = logging.getLogger('werkzeug')
    werkzeug_log.setLevel(logging.INFO)
    werkzeug_log.addHandler(file_handler)

from app import routes