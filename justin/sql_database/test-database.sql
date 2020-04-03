DROP TABLE IF EXISTS playlist_songs;
DROP TABLE IF EXISTS playlist;
DROP TABLE IF EXISTS lyrics;
DROP TABLE IF EXISTS album_songs;
DROP TABLE IF EXISTS album_user_likes;
DROP TABLE IF EXISTS artist_albums;
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS song;
DROP TABLE IF EXISTS artist_songs;
DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
    _id           INTEGER PRIMARY KEY,
    `name`        TEXT NOT NULL,
    email         TEXT NOT NULL,
    date_of_birth TEXT NOT NULL,
    `password`    TEXT NOT NULL
);

CREATE TABLE artist (
    _id           INTEGER PRIMARY KEY,
    `name`        TEXT NOT NULL
);

CREATE TABLE artist_songs (
    _id             INTEGER PRIMARY KEY,
    artist_id       INTEGER,
    song_id         INTEGER,
    FOREIGN KEY (song_id) REFERENCES song(_id)
    FOREIGN KEY (artist_id) REFERENCES artist(_id)
);

CREATE TABLE song (
    _id         INTEGER PRIMARY KEY,
    title       TEXT NOT NULL,
    artist_id   INTEGER,
    duration    REAL NOT NULL,
    release_year TEXT NOT NULL,
    likes       INTEGER
);

CREATE TABLE album (
    _id         INTEGER PRIMARY KEY,
    cover_image TEXT,
    title       TEXT,
    genre       TEXT,
    release_year TEXT,
);

CREATE TABLE artist_albums (
    _id         INTEGER PRIMARY KEY,
    artist_id       INTEGER,
    album_id    INTEGER,
    FOREIGN KEY (album_id) REFERENCES album(id),
    FOREIGN KEY (artist_id) REFERENCES artist(_id)
);

CREATE TABLE album_user_likes (
    _id         INTEGER PRIMARY KEY,
    album_id    INTEGER,
    user_id     INTEGER,
    FOREIGN KEY (album_id) REFERENCES album(id),
    FOREIGN KEY (user_id) REFERENCES user(_id)
);

CREATE TABLE album_songs(
    _id         INTEGER PRIMARY KEY,
    album_id    INTEGER,
    song_id     INTEGER,
    FOREIGN KEY (song_id) REFERENCES song(_id),
    FOREIGN KEY (album_id) REFERENCES album(id)
);

CREATE TABLE lyrics (
    _id         INTEGER PRIMARY KEY,
    song_id     INTEGER,
    `language`    TEXT NOT NULL,
    lyrics      TEXT NOT NULL,
    FOREIGN KEY (song_id) REFERENCES song(_id)
);

CREATE TABLE playlist (
    _id         INTEGER PRIMARY KEY,
    user_id     INTEGER,
    title       TEXT NOT NULL,
    song_id     INTEGER,
    FOREIGN KEY (user_id) REFERENCES user(_id)
);

CREATE TABLE playlist_songs (
    _id         INTEGER PRIMARY KEY,
    playlist_id INTEGER,
    song_id     INTEGER,
    FOREIGN KEY (playlist_id) REFERENCES playlist(_id),
    FOREIGN KEY (song_id) REFERENCES song(_id)

);