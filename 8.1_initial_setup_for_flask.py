'''
Server needs to be configured to allow access as a website using ip address
Need apache2 - mysqlclient - mysqlserver
sudo apt-get install apache2
sudo apt-get install mysql-client (if not already installed)
sudo apt-get install mysql-server (if not already installed)
Apache is the web server - back end for website - most popular
Want to have lib apache mod wsgi - flask uses wsgi to power website
sudo apt-get install libapache2-mod-wsgi - need to use libapache2-mod-wsgi-py3 for python3
This will restart web server
Need to enable wsgi
sudo a2enmod wsgi
cd var/www - directory when most people store web files
sudo mkdir [file name e.g.FlaskApp] - creates dictionary in file directory
cd FlaskApp/
sudo mkdir FlaskApp
cd FlaskApp/
- FlaskApp directory within FlaskApp folder
Make a couple of directories e.g. static 
sudo mkdir static - static files - can be accessed by anyone (unprotected) e.g. pythonprogramming.net/static
sudo mkdir templates - html files - structure of web page - home page / about page etc. - cannot be accessed (protected)
ls - view new directories
sudo nano __init__.py - creates main file for the website - can link to other files to build site

'''
from Flask import Flask

app = Flask(__name__) #name of app e.g. if name = main

@app.route('/') #if on a page e.g. google.com/ - / is decorator
def homepage():
    return "Hello World!"

if __name__ == "__main__":
    app.run()