--this is written in SQLite3 syntax
DROP TABLE IF EXISTS playlist_songs;
DROP TABLE IF EXISTS playlist;
DROP TABLE IF EXISTS lyrics;
DROP TABLE IF EXISTS song;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
    _id           INTEGER PRIMARY KEY,
    `name`        TEXT NOT NULL,
    email         TEXT NOT NULL,
    date_of_birth TEXT NOT NULL,
    `password`    TEXT NOT NULL
);

CREATE TABLE song (
    _id         INTEGER PRIMARY KEY, --replace with natural song primary key
    title       TEXT NOT NULL,
    artist      TEXT NOT NULL,
    duration    REAL NOT NULL,
    release_year TEXT NOT NULL,
    likes       INTEGER
);

CREATE TABLE lyrics (
    _id         INTEGER PRIMARY KEY,
    song_id     INTEGER,
    `language`    TEXT NOT NULL,
    FOREIGN KEY (song_id) REFERENCES song(id)
);

CREATE TABLE playlist (
    _id         INTEGER PRIMARY KEY,
    user_id     INTEGER,
    title       TEXT NOT NULL,
    song_id     INTEGER,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE playlist_songs (
    playlist_id INTEGER,
    song_id     INTEGER,
    FOREIGN KEY (playlist_id) REFERENCES playlist(id),
    FOREIGN KEY (song_id) REFERENCES song(id)

);