from flask import Blueprint, render_template, request, url_for, redirect
from .. import db
from ..Src.album import Album
from ..Src.song import Song
users = Blueprint("users", __name__)


@users.route("/user/mp", methods=["get"])
def get_all_song():
    all_song = Song.query.all()
    print(all_song[0].url)
    return render_template("player.html", song=all_song)


@users.route("/user/album", methods=["get"])
def get_all_album():
    all_album = Album.query.all()
    print(all_album)
    return render_template("player.html", album=all_album)


@users.route("/user/music_detail", methods=["post"])
def get_song_detail():
    data = request.form
    detail_song = Song.query.filter_by(id=int(data["id"])).first()
    print(detail_song)
    return render_template("player.html", detail=detail_song)


@users.route("/user/addsong", methods=["post"])
def add_song():
    # # print("hello")
    # # data = request.form
    # # print(data)
    # song = Song(
    #     url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    # add_song_function(song)
    data = request.form
    song = Song(url=data["Song_link"], img=data["Img_link"],
                name=data["name"], author=data["artist"], album=data['album'], lyrics=data["lyrics"], year=data["year"])
    add_song_function(song)
    return redirect(url_for("users.get_all_song"))


@users.route("/user/updatesong", methods=["post"])
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


@users.route("/user/music_delete", methods=['post'])
def delete_song():
    data = request.form
    db.session.query(Song).filter_by(id=int(data["id"])).delete()
    db.session.commit()
    return redirect(url_for("users.get_all_song"))


@users.route("/user/select_form", methods=["post"])
def Body_change():
    data = request.form
    if data["options"] == "Song":
        return redirect(url_for("users.get_all_song"))
    else:
        return redirect(url_for("users.get_all_album"))


def add_song_function(song):
    db.session.add(song)
    db.session.commit()
    print("add success")
