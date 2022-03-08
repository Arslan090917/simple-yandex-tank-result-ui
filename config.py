import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'yandex-tank_result.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST = '127.0.0.1'
    PORT = 44551
    PROXIES = None
    JSON_SORT_KEYS = False