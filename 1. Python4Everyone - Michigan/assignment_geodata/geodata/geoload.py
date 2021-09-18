import urllib.request, urllib.parse, urllib.error
import sqlite3
import json
import time
import ssl

serviceurl = "http://py4e-data.dr-chuck.net/json?"
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

fh = open("where.data")
count = 0
for line in fh:
    address = line.strip()
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    parms = dict()
    parms["address"] = address
    url = serviceurl + urllib.parse.urlencode(parms)

    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    count = count + 1

    js = json.loads(data)


    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
