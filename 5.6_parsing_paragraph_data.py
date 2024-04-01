import time
import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.urlopen('https://feeds.bbci.co.uk/sport/football/rss.xml')

xml = BeautifulSoup(req, 'xml')

for item in xml.findAll('link')[3:]: #[3:] Ignores first 3 links
    url = item.text
    news = urllib.request.urlopen(url).read()
    
    page = BeautifulSoup(news)
    
    for p in page.findAll('p'): #Find all references to p in tags
        print(p.text)
        
    time.sleep(10)