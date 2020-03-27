from flask import Blueprint, render_template, request, url_for, redirect, current_app
from .. import db
from ..Src.album import Album
from ..Src.song import Song
import pylast
import os
from .helper_method.helper import get_info
import boto3

users = Blueprint("users", __name__)
get_info = get_info()


@users.route("/user/Song", methods=["get"])
def get_all_song():
    all_song = Song.query.all()
    print(all_song)
    if(all_song):
        return render_template("player.html", song=all_song, s="a")
    else:
        return render_template("player.html")


@users.route("/user/album", methods=["get"])
def get_all_album():
    all_album = Album.query.all()
    print(all_album)
    return render_template("player.html", album=all_album, a="s")


@users.route("/user/music_detail", methods=["post"])
def get_song_detail():
    data = request.form
    detail_song = Song.query.filter_by(_Song__id=data["id"]).first()
    print(detail_song)
    return render_template("player.html", detail=detail_song)


@users.route("/user/addsong", methods=["post"])
def add_song():
    data = change_to_default(request.form)
    img = get_info.get_song_cover(data["artist"], data["name"])
    time = get_info.get_duration(data["artist"], data["name"])
    year = get_info.get_Track_date(data["artist"], data["name"])
    if data["album"] == None:
        data["album"] = "unknow"
    belongs_to = Album.query.filter_by(name=data["album"]).first()
    if belongs_to:
        song = Song(url=data["Song_link"], img=img, alb_img=belongs_to.cover_img,
                    name=data["name"], author=data["artist"], album_id=belongs_to._Album__id, album=belongs_to.name, duration=time, lyrics=data["lyrics"], year=year)
        add_song_function(song)
        return redirect(url_for("users.get_all_song"))
    else:
        return ("it seems like there is not ablum for it, please add the album first")


@users.route("/user/addalbum", methods=["post"])
def add_album():
    data = change_to_default(request.form)
    img_link = get_info.get_cover_art(data["artist"], data["name"])
    date = get_info.get_date(data["artist"], data["name"])
    style = get_info.get_style(data["artist"], data["name"])
    print(style)
    if data["name"] == None:
        data["name"] = "unknow"
        img_link = None
    is_album = Album.query.filter_by(name=data["name"]).first()
    if is_album:
        return ("Album is already exist, please check again")
    else:
        add_song_function(
            Album(cover_img=img_link, name=data["name"], author=data["artist"], genre=style, year=date))
    return redirect(url_for("users.get_all_album"))


@users.route("/user/updatesong", methods=["post"])
def update_song():
    data = request.form
    stmt = {"name": data["name"],
            "author": data["author"],
            "album": data["Album"],
            "lyrics": data["lyrics"]}
    db.session.query(Song).filter_by(_Song__id=data["id"]).update(stmt)
    db.session.commit()
    return ("Song successfully update")


@users.route("/user/music_delete", methods=['post'])
def delete_song():
    data = request.form
    db.session.query(Song).filter_by(_Song__id=data["id"]).delete()
    db.session.commit()
    return redirect(url_for("users.get_all_song"))


@users.route("/user/all_song_in_album", methods=['post'])
def song_in_album():
    album_id = request.form["id"]
    song_in_album = db.session.query(Song).filter_by(album_id=album_id).all()
    return render_template("player.html", song=song_in_album)


@users.route("/user/delete_album", methods=['post'])
def delete_album():
    data = request.form
    db.session.query(Album).filter_by(_Album__id=data["id"]).delete()
    db.session.commit()
    return redirect(url_for("users.get_all_album"))


@users.route("/user/select_form", methods=["post"])
def Body_change():
    data = request.form
    if data["options"] == "Song":
        return redirect(url_for("users.get_all_song"))
    else:
        return redirect(url_for("users.get_all_album"))


@users.route("/user/img_upload", methods=["POST"])
def upload():
    if request.files:
        f = request.files.get('file')
        if allow_file(f.filename):
            # path = os.path.join(current_app.config["IMG_UPLOAD"], f.filename)
            # f.save(path)
            s3 = boto3.resource("s3")
            s3.Bucket("apple-clone").put_object(Key=f.filename, Body=f)
            return f"https://apple-clone.s3-us-west-2.amazonaws.com/{f.filename}"
        else:
            return "image type is not supported, submit another one", 400


def add_song_function(song):
    db.session.add(song)
    db.session.commit()
    print("add success")


def change_to_default(dic):
    dicw = {}
    for k, v in dic.items():
        if v == "":
            dicw[k] = None
        else:
            dicw[k] = v
    return dicw


def allow_file(filename):
    Allow_list = ["MP3", "OGG", "WAV"]

    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in Allow_list:
        return True
    else:
        return False
