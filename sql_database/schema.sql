--this is written in SQLite3 syntax
DROP TABLE IF EXISTS playlists;
DROP TABLE IF EXISTS lyrics;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    _id           INTEGER PRIMARY KEY AUTOINCREMENT,
    `name`        TEXT NOT NULL,
    email         TEXT NOT NULL,
    date_of_birth TEXT NOT NULL,
    `password`    TEXT NOT NULL
);

CREATE TABLE songs (
    _id         INTEGER PRIMARY KEY AUTOINCREMENT, --replace with unique song tag ISRC so we don't need to worry about duplication**
    title       TEXT NOT NULL,
    artist      TEXT NOT NULL,
    duration    REAL NOT NULL,
    release_year TEXT NOT NULL,
    likes       INTEGER
);

CREATE TABLE lyrics (
    _id         INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id     INTEGER,
    `language`    TEXT NOT NULL,
    FOREIGN KEY (song_id) REFERENCES songs (id)
);

CREATE TABLE playlists (
    _id         INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     INTEGER,
    song_id     INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (song_id) REFERENCES songs (id)
);