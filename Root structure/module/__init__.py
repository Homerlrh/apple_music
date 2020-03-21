from flask import Flask, Blueprint, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)

    from .blueprints.index_route import main
    app.register_blueprint(main)

    with app.test_request_context():
        db.create_all()
    return app
