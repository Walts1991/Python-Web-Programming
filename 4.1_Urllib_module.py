#Urllib is a built-in Python module
#Library for URLs
#Access websites, read data, make requests and change headers (information sent to server)

import urllib.request #request for data on server on port 80 by default (default port for http/https data)

req =  urllib.request.urlopen('https://www.google.com')
print(req.read())
