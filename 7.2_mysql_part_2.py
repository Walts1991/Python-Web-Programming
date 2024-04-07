'''

To access mysql:
    mysql --user=root -p
    [no password]

To insert values into table:
INSERT INTO [table name] ([column1],[column2],[column3]) VALUES ([value1],[value2],[value3]);
INSERT INTO Programmers (name, language, email) VALUES ('Jay','Python','jay-k@g.com');
Need to put VARCHAR strings in quotes - do not need to quote integers

To show all rows in table:
SELECT * FROM [table name];
SELECT * FROM Programmers;

To show top 2 rows in table:
SELECT * FROM [table name] LIMIT [#]
SELECT * FROM Programmers LIMIT 2;

To show specific rows using filter:
SELECT * FROM [table name] WHERE [condition];
SELECT * FROM Programmers WHERE name = 'Jay;

To show specific [email] records using filter:
SELECT [column name] FROM [table name] WHERE [condition];
SELECT email FROM Programmers WHERE name = 'Jay;

To delete a specific row:
DELETE FROM [table name] where [condition];
DELETE FROM Programmers WHERE name = 'Jay';

To modify a value:
UPDATE [table name] Set  [column name] = 'new value' WHERE [condition];
UPDATE Programmers SET Name = 'Jason' WHERE name = 'Jay'

May want to modify table in the future
To delete everything from a table
DELETE FROM [table name];
DELETE FROM Programmers;

Preferred option is to use truncate - clears contents from table without deleting table:
TRUNCATE [table name];
TRUNCATE Programmers;

To delete table:
DROP TABLE [table name];
DROP TABLE Programmers;

To exit MySQL:
    Ctrl + d
'''
