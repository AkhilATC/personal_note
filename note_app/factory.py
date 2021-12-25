from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_note_space.sqlite3'
db = SQLAlchemy(app)

def create_app():

    from apps.controller import note_module
    app.register_blueprint(note_module)
    return app
