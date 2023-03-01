import sys
import os
import psycopg2

conn = None

try:
    conn = psycopg2.connect(database = sys.argv[1], user = os.environ.get('PGUSER'), password = os.environ.get('PGPASSWORD'), host = os.environ.get('PGHOST'), port = os.environ.get('PGPORT'))
    cur = conn.cursor()
    fh = open('number.txt','r')
    x = int(fh.read())
    yr= 2004 + 4*x
    fh.close()
    cur.execute('select isbn_no from book_catalogue where year='+str(yr))
    table = cur.fetchall()
    #print(type(table[0]))
    for row in table:
        print(row[0])
    cur.close()
except (Exception, psycopg2.DatabaseError) as err:
    print(err)
finally:
    conn.close()
