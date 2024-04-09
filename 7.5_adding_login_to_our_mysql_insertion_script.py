'''
#insertion2.py
'''

from bs4 import BeautifulSoup
import time
import urllib.request
from dbconnect import connection

req = urllib.request.urlopen('https://feeds.bbci.co.uk/sport/football/rss.xml')

xml = BeautifulSoup(req, 'xml')

conn, c = connection()

for item in xml.findAll('link')[3:]:
    url = item.text

    #Check if url exists in database
    c.execute("SELECT * FROM Links WHERE Link = (%s)",
              (url))

    #Fetch all rows which are included in database
    rows = c.fetchall()

    #If url is not within rows then execute script to insert urls
    if len(rows) == 0:
        c.execute("INSERT INTO links (time, link) VALUES (%s, %s)",
              (time.time(), link))
        conn.commit()
        print("Found a new link!")
    else:
        print("Link already in database")

conn.close()