'''
Flask is not a standard library in python
Need to ensure server is up to date 
sudo apt-get update
sudo apt-get upgrade
Ensure that pip is also installed
sudo apt-get install python-pip (use python3-pip for Python3)
Install virtual environment using pip:
sudo pip install virtualenv sudo virutalenv venv - did not work in server see below
python3 -m venv [file path e.g. var/www/FlaskApp/FlaskApp/venv]
virtual environment allows easier transfer between servers etc
also allows separate maintenance of modules etc
ls - see venv directory
venv directory includes bin/lib/local
To access virtual environment:
source venv/bin/activate
(venv) at start of file path shows user is in virtual environment
can install modules etc in virtual environment
sudo pip install Flask - may not need to use Sudo if using root user
Error reporting with flask when adding to __init__.py file is not great
To check code before going live:
sudo python __init__.py (may need to use Python3) - may not need to use Sudo if using root user
deactivate - to close virtual environment

To set up FLask configuration file:
sudo nano /etc/apache2/sites-available/FlaskApp.conf - Creates Flask config file
<VirtualHost *:80> - Port 80
    ServerName 46.101.82.121 - IP address for site
    ServerAdmin walts1991@googlemail.com - Admin email address
    WSGIScriptAlias / /var/www/FlaskApp/FlaskApp.wsgi - Directory of WSGI file
</VirtualHost>
[See next section]
'''