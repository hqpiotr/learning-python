# SQL + input file reading
# read the file
# count number of emails per organization/mail address domain
# put to database to maintain
import sqlite3
import re


def v2_read_input_write_db(fn):
    f = open(fn, 'r')
    sqldb = sqlite3.connect('Counts.sqlite')
    sqlptr = sqldb.cursor()

    """
    sqlptr.executescript('''
    DROP TABLE IF EXISTS tab1
    ''')
    """
    sqlptr.execute('DROP TABLE IF EXISTS Counts')
    sqlptr.execute('''CREATE TABLE Counts(org TEXT, count INTEGER)''')

    for line in f:
        if line.startswith('From: '):
            words = line.split()
            organization = re.sub('^.+@', '', words[1])

            sqlptr.execute('''SELECT * FROM Counts WHERE org=?''', (organization, ))
            row = sqlptr.fetchone()
            if row is None:
                sqlptr.execute('''INSERT INTO Counts(org, count) VALUES(?, 1)''', (organization, ))
            else:
                sqlptr.execute('''UPDATE Counts SET count=count+1 WHERE org=?''', (organization, ))
        else:
            continue

    sqlptr.execute('''SELECT * FROM Counts ORDER BY count DESC LIMIT 1''')
    result = sqlptr.fetchone()
    print(result[0], 'sent', result[1], 'mails.')

    sqldb.commit()
    sqldb.close()



if __name__ == "__main__":
    fn = 'input/mbox.txt'
    v2_read_input_write_db(fn)
