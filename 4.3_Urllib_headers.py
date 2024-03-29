#header contains information on browser,location,IP address etc in user agent
#Many websites shut out machines to avoid excess load
#Websites may offer an API - Application programmer interface
#APIs allow programs to access service in a more efficient manner
#API is preferred method to the below
#rss feeds used if URLs not known e.g. news feed

import urllib.request #request for data on server on port 80 by default (default port for http/https data)
import urllib.parse #handles URL encoding e.g. spaces within URL

values = {'q':'python programming tutorials'}

data = urllib.parse.urlencode(values)
url = 'https://www.google.com/search?q=' + data
#data = data.encode('utf-8')

#OOP - class(self, *args, **kwargs)
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

req = urllib.request.Request(url, headers=headers) #headers=headers is a kwarg (key word argument)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)
