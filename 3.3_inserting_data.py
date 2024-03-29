import sqlite3

conn = sqlite3.connect('3.3.tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")

def enter_data():
    c.execute("INSERT INTO example VALUES('Python', '2.7', 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', '3.3', 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Python', '3.4', 'Expert')")
    conn.commit() #Saves the values into the database

create_table()

enter_data()

conn.close()
