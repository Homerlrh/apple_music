from flask import Flask, Blueprint, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os

basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config["SECRET_KEY"] = "$2y$04$RsF3IDeklJqOHS/GV7JaSeZtUwUKSX/oqAZRQurtHSnxNo3a4M3fC"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)
    Bootstrap(app)
    from .blueprints.index_route import main
    app.register_blueprint(main)
    from .blueprints.users_route import users
    app.register_blueprint(users)
    with app.test_request_context():
        db.create_all()
    return app
