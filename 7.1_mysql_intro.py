#
'''
Login to server via Putty/Console
Need to install mysql on server
mysql comes in two parts
- mysql client - used to interact with mysql
- mysql server - used to run mysql
sudo - stands for superuser
sudo apt-get install mysql-client
sudo apt-get install mysql-server
Should ask for password for root user (different to VPS) - did not happen during setup
To access mysql:
    mysql --user=root -p
    [no password]
End all commands with a ;
SHOW DATABASES; - Used to show existing databases in MySQL
CREATE DATABASE [Name]; - Creates a new database
CREATE DATABASE [Test]
Database is a collection of tables
USE Test; - Enter database
CREATE TABLE [name] ([Column] [DATATYPE(),..]); - Tables have multiple columns separated by commas
CREATE TABLE Programmers (Name VARCHAR(20), Language VARCHAR(20), Email VARCHAR(50));
mySQL has over.100 data types - VARCHAR is variable length string, INT is integer etc.
Datatypes can affect performance on large databases
FLOAT([Length],[decimals])
SHOW TABLES; - Used to show existing tables in MySQL
DESCRIBE [Table_name]; - Shows the structure and details of each column in table
'''
