import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # uri for sql lite database
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
=======
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')

    # uri for postgres local database
    # not for Heroku usage yet
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:po_admin@localhost:5434/ecommerce'
>>>>>>> pg_local
