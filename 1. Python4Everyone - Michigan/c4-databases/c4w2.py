# SQL
import sqlite3

"""
        INSERT INTO Users (param1, param2) VALUES (val1, val2)
        DELETE FROM Users WHERE email='someone@yahoo.com'
        UPDATE Users SET name='DonPedro' WHERE email='piotr@someone.com'
        
        SELECT * FROM Users
        SELECT * FROM Users WHERE email='piotr@someone.com'
        SELECT * FROM Users ORDER BY email
"""

connection = sqlite3.connect('mydb.sqlite')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Counts')
cursor.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

file = open('input/mbox-short.txt')
for line in file:
    if not line.startswith('From: '): continue
    # store email
    words = line.split()
    email = words[1]

    # check if record exists with such email
    cursor.execute('SELECT count FROM Counts WHERE email = ?', (email, ))
    row = cursor.fetchone()
    # if not, create it
    if row is None:
        cursor.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email, ))
    # if exists, update the count of sent emails
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email, ))

    #commit
    connection.commit()

# query
query = 'SELECT email, count FROM Counts ORDER BY count DESC limit 10'

# print db with query
for row in cursor.execute(query):
    print(str(row[0]), row[1])

# close
connection.close()
