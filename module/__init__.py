from flask import Flask, Blueprint, render_template, request, jsonify
from flask_dropzone import Dropzone
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)

db = SQLAlchemy()


def create_app():
    load_dotenv()
    app = Flask(__name__, template_folder="templates")
    app.config["SECRET_KEY"] = os.getenv("S_K")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_uri")
    # app.config["IMG_UPLOAD"] = "module\static\img"
    db.init_app(app)
    Bootstrap(app)
    dropzone = Dropzone(app)
    from .blueprints.index_route import main
    app.register_blueprint(main)
    from .blueprints.users_route import users
    app.register_blueprint(users)
    with app.test_request_context():
        db.create_all()
    return app
