--this is written in SQLite3 syntax
DROP TABLE IF EXISTS playlist_songs;
DROP TABLE IF EXISTS playlists;
DROP TABLE IF EXISTS lyrics;
DROP TABLE IF EXISTS album_songs;
DROP TABLE IF EXISTS album_user_likes;
DROP TABLE IF EXISTS artist_albums;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS user_favorite_songs;
DROP TABLE IF EXISTS song_user_likes;
DROP TABLE IF EXISTS artist_songs;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    _id           INTEGER PRIMARY KEY,
    email         TEXT NOT NULL,
    password_hash    TEXT NOT NULL,
    `name`        TEXT NOT NULL,
    date_of_birth TEXT NOT NULL
);

CREATE TABLE artists (
    _id           INTEGER PRIMARY KEY,
    `name`        TEXT NOT NULL
);

CREATE TABLE songs (
    _id         INTEGER PRIMARY KEY,
    title       TEXT NOT NULL,
    artist_id   INTEGER,
    duration    REAL NOT NULL,
    release_year TEXT NOT NULL
);

--artists have many songs, and songs can be recorded by many artists
CREATE TABLE artist_songs (
    _id             INTEGER PRIMARY KEY,
    artist_id       INTEGER,
    song_id         INTEGER,
    FOREIGN KEY (song_id) REFERENCES songs(_id),
    FOREIGN KEY (artist_id) REFERENCES artists(_id)
);

CREATE TABLE song_user_likes (
    _id         INTEGER PRIMARY KEY,
    song_id    INTEGER,
    user_id     INTEGER,
    FOREIGN KEY (song_id) REFERENCES song(_id),
    FOREIGN KEY (user_id) REFERENCES users(_id)
);

CREATE TABLE user_favorite_songs (
    _id           INTEGER PRIMARY KEY,
    user_id       INTEGER,
    song_id         INTEGER,
    FOREIGN KEY (song_id) REFERENCES songs(_id),
    FOREIGN KEY (user_id) REFERENCES users(_id)
);

CREATE TABLE albums (
    _id         INTEGER PRIMARY KEY,
    title       TEXT,
    genre       TEXT,
    release_year TEXT,
    cover_image TEXT
);

--artists have many albums and albums with the same name could be re-recorded/reproduced by another artist
CREATE TABLE artist_albums (
    _id         INTEGER PRIMARY KEY,
    artist_id       INTEGER,
    album_id    INTEGER,
    FOREIGN KEY (album_id) REFERENCES albums(_id),
    FOREIGN KEY (artist_id) REFERENCES artists(_id)
);

--albums have many likes by users, users like many albums
CREATE TABLE album_user_likes (
    _id         INTEGER PRIMARY KEY,
    album_id    INTEGER,
    user_id     INTEGER,
    FOREIGN KEY (album_id) REFERENCES albums(_id),
    FOREIGN KEY (user_id) REFERENCES users(_id)
);

--albums have many songs, songs can exist in many albums
CREATE TABLE album_songs(
    _id         INTEGER PRIMARY KEY,
    album_id    INTEGER,
    song_id     INTEGER,
    FOREIGN KEY (song_id) REFERENCES songs(_id),
    FOREIGN KEY (album_id) REFERENCES albums(_id)
);

CREATE TABLE lyrics (
    _id         INTEGER PRIMARY KEY,
    song_id     INTEGER,
    `language`    TEXT NOT NULL,
    lyrics      TEXT NOT NULL,
    FOREIGN KEY (song_id) REFERENCES songs(_id)
);

CREATE TABLE playlists (
    _id         INTEGER PRIMARY KEY,
    user_id     INTEGER,
    title       TEXT NOT NULL,
    song_id     INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(_id)
);

--playlists have many songs, songs exist in many playlists
CREATE TABLE playlist_songs (
    _id         INTEGER PRIMARY KEY,
    playlist_id INTEGER,
    song_id     INTEGER,
    FOREIGN KEY (playlist_id) REFERENCES playlists(_id),
    FOREIGN KEY (song_id) REFERENCES songs(_id)

);