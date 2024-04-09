from bs4 import BeautifulSoup
import time
import urllib.request
from dbconnect import connection

req = urllib.request.urlopen('https://feeds.bbci.co.uk/sport/football/rss.xml')

xml = BeautifulSoup(req, 'xml')

conn, c = connection()  # Unpack returned connection and cursor

def parse_links():
    for item in xml.findAll('link')[3:]:
        url = item.text

        # Check if url exists in database
        c.execute("SELECT * FROM Links WHERE Link = (%s)", (url,))

        # Fetch all rows which are included in database
        rows = c.fetchall()

        # If url is not within rows then execute script to insert urls
        if len(rows) == 0:
            c.execute("INSERT INTO Links (time, link) VALUES (%s, %s)", (time.time(), url))
            conn.commit()
            print("Found a new link!")
        else:
            #print(rows)
            print("Link already in database")
            
        time.sleep(10)

    conn.close()

for True:
    
    parse_links()