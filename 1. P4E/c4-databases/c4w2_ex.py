"""
    This application will read the mailbox data (mbox.txt) and count the number
    of email messages per organization (i.e. domain name of the email address)
    using a database with the following schema to maintain the counts.
"""
import urllib.request
import sqlite3
import ssl
import re

# read the file
# count number of emails per organization/mail address domain
# put to database to maintain

def read_file_write_db(filename):
    sqldb = sqlite3.connect('FirstCounts.sqlite')
    sqlptr = sqldb.cursor()
    sqlptr.execute('''DROP TABLE IF EXISTS Counts''')
    sqlptr.execute('''CREATE TABLE Counts (org TEXT, mails INTEGER)''')

    file = open(filename, 'r')


    for line in file:
        if not line.startswith('From: '):
            continue
        else:
            splitline = line.split()
            organization = splitline[1]
            organization = re.sub(r'^.+@', '', organization)
            # print(organization)

            sqlptr.execute('SELECT * FROM Counts WHERE org=?', (organization,))
            row = sqlptr.fetchone()
            if row is None:
                sqlptr.execute('INSERT INTO Counts (org, mails) VALUES(?, 1)', (organization,))
            else:
                sqlptr.execute('UPDATE Counts SET mails=mails+1 WHERE org=?', (organization,))

    for i in sqlptr.execute('SELECT * FROM Counts ORDER BY mails DESC LIMIT 1'):
        print(i)

    sqldb.commit()
    sqldb.close()




if __name__ == "__main__":
    # link = "https://www.py4e.com/code3/mbox.txt" # doesn't work: HTTP Error 403: Forbidden (even with CERT)
    file = 'input/mbox.txt'
    read_file_write_db(file)