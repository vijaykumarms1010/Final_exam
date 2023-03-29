import os

DEBUG = True
SECRET_KEY = 'secretKey!'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'inventory.db')