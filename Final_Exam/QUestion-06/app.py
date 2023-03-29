from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import json

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
#

from routes import *
with app.app_context():
   db.create_all()
#
if __name__ == '__main__':
    app.run()