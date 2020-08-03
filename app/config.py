import os

# configuraciones. True para que el servidor pueda ser levantado en modo debug
DEBUG = True

# configuracion BD
""""
SECRET_KEY =  'A SECRET KEY'
SQLALCHEMY_TRACK_MODIFICATIONS = False
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'models/trivia.db')
"""

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'trivia',
    'host': 'localhost',
    'port': '5432',
}
SECRET_KEY = 'pepesecreto'
SQLALCHEMY_TRACK_MODIFICATIONS = False

#postgresql://username:password@hostname/database
SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES['user']}:" \
                          f"{POSTGRES['pw']}@{POSTGRES['host']}:" \
                          f"{POSTGRES['port']}/{POSTGRES['db']}"

