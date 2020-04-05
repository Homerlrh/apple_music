from flask import Blueprint, render_template, request, url_for, redirect,make_response
from sqlalchemy.sql.expression import bindparam
from .. import db
from ..Src.user import user
import jwt
import datetime


main = Blueprint("main", __name__)


@main.route("/", methods=['get'])
def index():
    return render_template("login.html")


@main.route("/login", methods=["post"])
def login():
    login_user = request.form
    print(login_user)
    if not login_user or not login_user['email'] or not login_user['password']:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm = "Login Required!"'})
    usr = user.query.filter_by(email = login_user['email']).first()

    if not usr:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm = "Login Required!"'})
    
    if usr.password == login_user['password']:
        token = jwt.encode({'user_email' : usr.email , 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'thisissecret')
        resp = make_response(redirect('/user/Song'))
        resp.set_cookie('user', token)

        return resp

        #return jsonify({'token' : token.decode('UTF-8')}) # The decode call here doesn't decode the jwt, it converts the encoded jwt from
                                                          # a byte string to a utf-8 string.
    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm = "Login Required!"'})



@main.route("/signup", methods=["post"])
def signup():
    data = request.form
    print(data)

    usr = user(email = data['email'], password = data['password'])
    db.session.add(usr)
    db.session.commit()

    resp = make_response(render_template('login.html'))
   
    return resp
    
