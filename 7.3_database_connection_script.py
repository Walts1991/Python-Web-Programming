'''
Script that will connect to mysql database
mysql database is protected by username/password
mysql is capable of remote connections

To install python mySQLdb:
sudo apt-get install python-MySQLdb - did not work
Bard - sudo apt install python3-dev default-libmysqlclient-dev build-essential  # For Python 3
or python3 -m pip install mysqlclient
or python -m pip install PyMySQL - different package

May need to create virtual environment - see Bard/Gemini chat history 07/04/2024

Within python interpreter:
import MySQLdb - care which capitalisation

Build database connection file
Issue connection and cursor to database
Import file to be used across multiple scripts

nano dbconnect.py - if in console
'''

import MySQLdb

def connection():
    conn = MySQLdb,connect(host='localhost',user='root',passwd='',db='Test')
    c = conn.cursor()
    return conn,c

if __name__ == '__main__':
    c, conn = connection()
    print("It worked!")
