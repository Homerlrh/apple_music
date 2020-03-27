from flask import Blueprint, render_template, request, url_for, redirect
from sqlalchemy.sql.expression import bindparam
from .. import db
from ..Src.user import user


main = Blueprint("main", __name__)


@main.route("/", methods=['get'])
def index():
    return render_template("login.html")


@main.route("/login", methods=["post"])
def login():
    data = request.form
    print(data)
    return data


@main.route("/signup", methods=["post"])
def signup():
    data = request.form
    return data
