'''
How to make program automatically find data and insert into database
Set up table in mysql

Connect to database
mysql --user=root -p
enter password (if any)

SHOW DATABASES;
USE Test;
SHOW TABLES;
CREATE TABLE Links (time FLOAT(18,2), link VARCHAR(400));
SHOE TABLES;
QUIT()

python
import bs4 - Install if necessary sudo apt install python3-bs4 in root / pip install bs4 in virtual environment
quit()

Create script file 0704.py
Renamed to insertion.py and saved on server in virtual environment
Navigate to directory
python insertion.py - to run script
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
    c.execute("INSERT INTO links (time, link) VALUES (%s, %s)",
              (time.time(), link))
    conn.commit()

conn.close()
