#http://www.nationaljournal.com/politics?rss=1 - Example XML rss file
#https://feeds.bbci.co.uk/sport/football/rss.xml - Another example

#Beautiful soup module is used for web scraping
#Pay attention to terms of service / copyright law re legality
#Similar to torrent programs

import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.urlopen('https://feeds.bbci.co.uk/sport/football/rss.xml')

xml = BeautifulSoup(req, 'xml') #Need to specify xml data - ensure lxml is installed via pip

for item in xml.findAll('link')[3:4]: #[3:5] Ignores first 3 links :5 limits to top link i.e 5-3 = 2 links
    print(item.text)
    url = item.text
    news = urllib.request.urlopen(url).read()
    print(news)
    print(20*"#")
