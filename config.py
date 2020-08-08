import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    SQLALCHEMY_DATABASE_URI = '{db_type}+{driver_name}://{user}:{password}@{host}/{name}'.format(
        db_type=os.environ.get('DB_TYPE'),
        driver_name=os.environ.get('DRIVER_NAME'),
        user=os.environ.get('USER'),
        password=os.environ.get('PASSWORD'),
        host=os.environ.get('HOST'),
        port=os.environ.get('PORT'),
        name=os.environ.get('DB_NAME'),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    DEBUG = True