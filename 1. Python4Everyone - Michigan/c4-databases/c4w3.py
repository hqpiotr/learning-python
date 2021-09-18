# SQL
import sqlite3

sqldb = sqlite3.connect('db.sqlite')
sqlptr = sqldb.cursor()

sqlptr.executescript('''
    SELECT Track.name, Album.title, Artist.name, Genre.type FROM
    Track JOIN Artist JOIN Album JOIN Genre ON
    Track.album_id = Album.id AND
    Album.artist_id = Artist.id
    
''')


sqlptr.executescript('''
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    
    CREATE TABLE Track(
        id INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY UNIQUE,
        title TEXT
        album_id INTEGER
        genre_id INTEGER
    );
    CREATE TABLE Album(
        id INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY UNIQUE,
        title TEXT
        artist_id INTEGER
    );
    CREATE TABLE Artist(
        id INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY UNIQUE,
        name TEXT
    );
    CREATE TABLE Genre( 
        id INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY UNIQUE,
        type TEXT
    );
    
    artist = lookup(line, 'artist')
    
    sqlptr.execute(INSERT OR IGNORE INTO Artist (name) VALUES (?), (artist, ))
    sqlptr.execute(SELECT id FROM Artist WHERE name = ?, (artist, ))
    artist_id = sqlptr.fetchone()[0]
    ...
    INSERT OR REPLACE - standard
    INSER OR IGNORE - non standard
    
    sqldb.commit()
    
''')
