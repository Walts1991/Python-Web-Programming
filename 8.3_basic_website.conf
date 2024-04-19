'''
To set up FLask configuration file:
sudo nano /etc/apache2/sites-available/FlaskApp.conf - Creates Flask config file
<VirtualHost *:80> - Port 80
    ServerName 46.101.82.121 - IP address for site
    ServerAdmin walts1991@googlemail.com - Admin email address
    WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi - Directory of WSGI file
    <Directory / var/www/FlaskApp/FlaskApp/>
        Order allow,dent
        Allow from all
    </Directory>
    Alias /static /var/www/FlaskApp/FlaskApp/static
    <Directory /var/www/FlaskApp/FlaskApp/static
        Order allow,dent
        Allow from all
    </Directory>   
    
    ErrorLog ${APACHE_LOG_DIR}/error.log - Create error log
    LogLevel warn - Set level of error logs to warnings
    CustomLog  ${APACH_LOG_DIR}/access.log combined - Combine date and time with
    
</VirtualHost>

To enable config file:
sudo a3ensite FlaskApp
service apache2 reload

[Resume video at 4 minutes]

'''
<VirtualHost *:80>
    ServerName 46.101.82.121
    ServerAdmin walts1991@googlemail.com
    WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
    <Directory /var/www/FlaskApp/FlaskApp/>
        Order allow,deny
        Allow from all
    </Directory>
    Alias /static /var/www/FlaskApp/FlaskApp/static
    <Directory /var/www/FlaskApp/FlaskApp/static>
        Order allow,deny
        Allow from all
    </Directory>   
    
    ErrorLog ${APACHE_LOG_DIR}/error.log
    LogLevel warn
    CustomLog  ${APACHE_LOG_DIR}/access.log combined
    
</VirtualHost>
