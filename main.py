from flask import Flask, render_template, request, jsonify

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()

admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')


@app.route("/")
def home():
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    return render_template("index.html")


@app.route("/login")
def login():
    # User.query.all()
    # name = User.query.filter_by(username='admin').first()
    # print(name)
    # return render_template("login.html", user=name)
    return render_template("index.html")


@app.route("/m", methods=["post"])
def sent():
    print("hello")
    data = request.form
    return data


@app.route("/mp", methods=["get"])
def play_music():
    return render_template("player.html")


if __name__ == "__main__":
    app.run(debug=True)
