DROP DATABASE IF EXISTS artist, album, song;

CREATE TABLE artist (
    artist_id INT PRIMARY KEY,
    artist_name VARCHAR(50)
);

CREATE TABLE album (
    album_id INT PRIMARY KEY,
    artist_id INT,
    album_title VARCHAR(100),
    FOREIGN KEY (artist_id) REFERENCES artist(artist_id),
);

CREATE TABLE song (
    song_id INT PRIMARY KEY,
    song_title VARCHAR(100),
    album_id INT,
    track_number INT,
    duration TIME,
    FOREIGN KEY (album_id) REFERENCES album(album_id)
);
