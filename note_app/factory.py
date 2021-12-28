from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from swagger_init import set_up_swagger



app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_note_space.sqlite3'
db = SQLAlchemy(app)

def create_app():

    from apps.controller import note_module
    app.register_blueprint(note_module)
    set_up_swagger(app)
    return app
