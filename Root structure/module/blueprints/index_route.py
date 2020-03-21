from flask import Blueprint, render_template, request
from sqlalchemy.sql.expression import bindparam
from .. import db
from ..Src.album import Album
from ..Src.song import Song

main = Blueprint("main", __name__)


@main.route("/", methods=['get'])
def index():

    return render_template("login.html")


@main.route("/m", methods=["post"])
def sent():
    print("hello")
    data = request.form
    return data


@main.route("/mp", methods=["get"])
def music_player():
    all_song = Song.query.all()
    print(all_song[0].url)
    return render_template("player.html", song=all_song)


@main.route("/addsong", methods=["get"])
def add_song():
    # print("hello")
    # data = request.form
    # print(data)
    song = Song(
        url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    add_song_function(song)
    return render_template("player.html")


@main.route("/updatesong", methods=["post"])
def update_song():
    # print("hello")
    data = request.form
    stmt = {"name": data["name"],
            "author": data["author"],
            "album": data["Album"],
            "lyrics": data["lyrics"]}
    db.session.query(Song).filter_by(id=int(data["id"])).update(stmt)
    db.session.commit()
    return ("Song successfully update")


@main.route("/music_detail", methods=["post"])
def get_song_detail():
    data = request.form
    detail_song = Song.query.filter_by(id=int(data["id"])).first()
    print(detail_song)
    return render_template("player.html", detail=detail_song)


def add_song_function(song):
    db.session.add(song)
    db.session.commit()
    print("add success")
