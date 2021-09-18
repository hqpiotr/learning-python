# SQL RDBMS, related tables
# XML
import sqlite3
import xml.etree.ElementTree as ET

# make an sqlite3 db with songs
# delete tables at start
# import input/Library.xml
# print table as below with 3 records sorted by artist.name
"""
Track	                                Artist  Album	        Genre
Chase the Ace	                        AC/DC	Who Made Who	Rock
D.T.	                                AC/DC	Who Made Who	Rock
For Those About To Rock (We Salute You)	AC/DC	Who Made Who	Rock
"""

"""
<dict>                      /dict #1
	<key>
	<key>
	<key>
	<key>
	<dict>                  /dict #2
		<key>369</key>
		<dict>              /dict #3
			<key>Track ID</key><integer>369</integer>
			<key>Name</key><string>Another One Bites The Dust</string>
			<key>Artist</key><string>Queen</string>
			<key>Album</key><string>Greatest Hits</string>
			<key>Genre</key><string>Rock</string>
		</dict>
		<key>370</key>
		<dict>              /dict #3
			<key>track ID
			<key>artist
			<key>album
			<key>
		</dict>
	</dict>
"""

def find_key(lines, key):
    found = False
    for l in lines:
        if found == True: return l.text
        if l.tag == 'key' and l.text == key:
            found = True
    return None


def read_xml_make_RDBMS(xmlfile):
    sqldb = sqlite3.connect('trackdb.sqlite')
    sqlptr = sqldb.cursor()

    sqlptr.executescript('''
        DROP TABLE IF EXISTS Artist;
        DROP TABLE IF EXISTS Album;
        DROP TABLE IF EXISTS Track;
        DROP TABLE IF EXISTS Genre;
        
        CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
        CREATE TABLE Album  (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE, artist_id INTEGER);
        CREATE TABLE Genre  (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
        CREATE TABLE Track  (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE, album_id INTEGER, 
                                                        genre_id INTEGER, len INTEGER, rating INTEGER, count INTEGER);
    ''')

    tree = ET.parse(xmlfile) # ==fromString
    values = tree.findall('dict/dict/dict')

    # For each line of dict tree, search for song details
    for v in values:
        if (find_key(v, 'Track ID') is None): continue # TODO: necessary

        v_name = find_key(v, 'Name')
        v_artist = find_key(v, 'Artist')
        v_album = find_key(v, 'Album')
        v_genre = find_key(v, 'Genre')
        v_count = find_key(v, 'Play Count')
        v_rating = find_key(v, 'Rating')
        v_length = find_key(v, 'Total Time')

        if v_name is None or v_artist is None or v_album is None or v_genre is None or\
           v_count is None or v_rating is None or v_length is None: continue

        # First put the artist to db, later on fetch it's ID for related DB. Do similar for other relations.
        sqlptr.execute('INSERT OR IGNORE INTO Artist(name) VALUES (?)', (v_artist,))
        common_artist_id = sqlptr.lastrowid #TODO: return last row ID returned with PRIMARY KEY (meaning ID)
        # sqlptr.execute('SELECT id FROM Artist WHERE name = ?', (v_artist,))
        # common_artist_id = sqlptr.fetchone()[0]

        sqlptr.execute('''INSERT OR IGNORE INTO Album(title, artist_id) VALUES (?, ?)''', (v_album, common_artist_id))
        # sqlptr.execute('SELECT id FROM Album WHERE title=?', (v_album,))
        # common_album_id = sqlptr.fetchone()[0]
        common_album_id = sqlptr.lastrowid

        sqlptr.execute('INSERT OR IGNORE INTO Genre(name) VALUES(?)', (v_genre, ))
        # sqlptr.execute('SELECT id FROM Genre WHERE name=?', (v_genre, ))
        # common_genre_id = sqlptr.fetchone()[0]
        common_genre_id = sqlptr.lastrowid

        sqlptr.execute('''
            INSERT OR REPLACE INTO Track(title, album_id, genre_id, len, rating, count) VALUES(?, ?, ?, ?, ?, ?)''',\
            (v_name, common_album_id, common_genre_id, v_length, v_rating, v_count ))

        sqldb.commit()
        print(v_name + "\t--\t" + v_artist + "\t--\t" + v_album + "\t--\t" + v_genre)
    sqldb.close()


if __name__ == "__main__":
    read_xml_make_RDBMS('input/Library.xml')

