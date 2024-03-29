import urllib.request #request for data on server on port 80 by default (default port for http/https data)
import urllib.parse #handles URL encoding e.g. spaces within URL

#Initial method - Method not allowed
"""
url = 'https://www.google.com/search'
values = {'q':'python programming tutorials'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') #Internet understands utf-8 so need to encode to send / decode for extract data

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)
"""

#Updated method - Forbidden
values = {'q':'python programming tutorials'}

data = urllib.parse.urlencode(values)
url = 'https://www.google.com/search?q=' + data
#data = data.encode('utf-8')

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)
