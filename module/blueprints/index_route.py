from flask import Blueprint, render_template, request, url_for, redirect, make_response
from sqlalchemy.sql.expression import bindparam
from .. import db
from ..Src.user import user


main = Blueprint("main", __name__)


@main.route("/", methods=['get'])
def index():
    try:
        newuser = user(name="admin", email="123@123.123", password="123123")
        db.session.add(newuser)
        db.session.commit()
        return render_template("login.html")
    except:
        return render_template("login.html")


@main.route("/login", methods=["post"])
def login():
    accound = request.form['email']
    password = request.form['password']
    try:
        is_user = db.session.query(user).filter_by(email=accound).first()
        if is_user:
            if is_user.password == password:
                resp = make_response(redirect("/user/Song"))
                resp.set_cookie('current_user', str(is_user._user__id))
                return resp
            else:
                return "password does not match, try again"
    except AttributeError:
        return "user is not exist"


@main.route("/signup", methods=["post"])
def signup():
    data = request.form

    return data


@main.route("/logout", methods=['GET'])
def logout():
    resp = make_response(redirect("/"))
    user_id = request.cookies.get("current_user")
    resp.set_cookie('user', user_id, max_age=0)
    return resp
