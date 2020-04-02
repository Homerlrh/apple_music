from flask import Blueprint, render_template, request, url_for, redirect, current_app
from .. import db
from ..Src.album import Album
from ..Src.song import Song
from .helper_method.helper import get_info
import boto3
import pylast
import os
from mutagen.mp3 import MP3

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
    print(request.form)
    data = change_to_default(request.form)
    print(data)
    img = get_info.get_song_cover(data["artist"], data["name"])
    year = get_info.get_song_date(data["artist"], data["name"])
    lyrics = get_info.get_lyrics(data["artist"], data["name"])
    belongs_to = Album.query.filter_by(
        name=data["album"]).filter_by(author=data["artist"]).first()
    if belongs_to:
        song = Song(url=data["Song_link"], img=img, alb_img=belongs_to.cover_img,
                    name=data["name"], author=data["artist"], album_id=belongs_to._Album__id, album=belongs_to.name, duration=data["duration"], lyrics=lyrics, year=year)
        add_song_function(song)
    else:
        song = Song(url=data["Song_link"], img=img, alb_img=None,
                    name=data["name"], author=data["artist"], album_id=None, album=None, duration=data["duration"], lyrics=lyrics, year=year)
        add_song_function(song)
    return redirect(url_for("users.get_all_song"))


@users.route("/user/addalbum", methods=["post"])
def add_album():
    data = change_to_default(request.form)
    img_link = get_info.get_cover_art(data["artist"], data["name"])
    date = get_info.get_date(data["artist"], data["name"])
    style = get_info.get_style(data["artist"], data["name"])
    if date != None:
        date = date.split(",")[0]
    # print(get_info.tryout())
    # return get_info.tryout()
    if data["name"] == None:
        data["name"] = "unknow"
        img_link = None
    # is_album = Album.query.filter_by(name=data["name"]).first()
    # if is_album:
    #     return ("Album is already exist, please check again")
    # else:
    add_song_function(Album(
        cover_img=img_link, name=data["name"], author=data["artist"], genre=style, year=date))
    return redirect(url_for("users.get_all_album"))


@users.route("/user/updatesong", methods=["post"])
def update_song():
    data = request.form
    is_album = db.session.query(Album).filter_by(name=data["Album"]).first()
    if is_album:
        a_id = is_album._Album__id
        img = is_album.cover_img
    else:
        a_id = None
        img = 'https://cdn3.iconfinder.com/data/icons/iconic-1/32/x_alt-512.png'
    stmt = {"name": data["name"],
            "author": data["author"],
            "album_id": a_id,
            "genre": data["genre"],
            "album": data["Album"],
            "lyrics": data["lyrics"],
            "alb_img": img}
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
    print(song_in_album.__len__())
    return render_template("player.html", song=song_in_album)


@users.route("/user/delete_album", methods=['post'])
def delete_album():
    data = request.form
    db.session.query(Album).filter_by(_Album__id=data["id"]).delete()
    # db.session.query(Song).filter_by(album_id=data["id"]).delete()
    db.session.commit()
    return redirect(url_for("users.get_all_album"))


@users.route("/user/select_form", methods=["post"])
def Body_change():
    data = request.form
    if data["options"] == "Song":
        return redirect(url_for("users.get_all_song"))
    else:
        return redirect(url_for("users.get_all_album"))


@users.route("/user/song_upload", methods=["POST"])
def upload():
    if request.files:
        f = request.files['file']
        if allow_file(f.filename):
            audio = MP3(f)
            duration = get_info.get_duration_2(audio.info.length)
            s3 = boto3.resource("s3")
            s3.Bucket("apple-clone").put_object(Key=f.filename, Body=f)
            info = {
                "time": duration,
                "url": f"https://d39wlfkh0mxxlz.cloudfront.net/{f.filename}",
            }
            return info
        else:
            return "Type is not supported, submit another one", 400


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
