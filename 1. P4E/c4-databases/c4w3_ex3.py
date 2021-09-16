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

    # prepare SQL databases
    sqlptr.executescript('''
        DROP TABLE IF EXISTS Artist;
        DROP TABLE IF EXISTS Album;
        DROP TABLE IF EXISTS Track;
        DROP TABLE IF EXISTS Genre;
        
        CREATE TABLE Artist(
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE);
        
        CREATE TABLE Album(
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title TEXT UNIQUE,
            artist_id INTEGER);
        
        CREATE TABLE Genre(
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE);
        
        CREATE TABLE Track(
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title TEXT UNIQUE,
            album_id INTEGER,
            genre_id INTEGER,
            len INTEGER, rating INTEGER, count INTEGER);
    ''')

    # Parse XML with dicts
    tree = ET.parse(xmlfile) # ==fromString
    values = tree.findall('dict/dict/dict')

    # For each line of dict tree, search for song details
    for v in values:
        # if (find_key(v, 'Track ID') is None): continue
        v_name = find_key(v, 'Name')
        v_artist = find_key(v, 'Artist')
        v_album = find_key(v, 'Album')
        v_count = find_key(v, 'Play Count')
        v_rating = find_key(v, 'Rating')
        v_length = find_key(v, 'Total Time')
        # print(v_name, v_artist, v_album, v_count, v_rating, v_length)

        # Put this data to relevant SQL databases
        sqlptr.execute('INSERT OR IGNORE INTO Artist(name) VALUES(?)', (v_artist, ))

        # Get the ID after insertion
        sqlptr.execute('SELECT id FROM Artist WHERE name=?', (v_artist, ))
        # Store it for reference
        artist_id = sqlptr.fetchone()[0]
        print(artist_id)


if __name__ == "__main__":
    read_xml_make_RDBMS('input/Library.xml')

