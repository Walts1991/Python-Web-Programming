from bs4 import BeautifulSoup
import time
import urllib.request
from dbconnect import connection

req = urllib.request.urlopen('https://feeds.bbci.co.uk/sport/football/rss.xml')

xml = BeautifulSoup(req, 'xml')

conn, c = connection()  # Correct variable assignment

for item in xml.findAll('link')[3:]:
    url = item.text  # Assign URL for each link
    c.execute("INSERT INTO Links (time, link) VALUES (%s, %s)", (time.time(), url))

    conn.commit()

conn.close()
