import sqlite3

conn = sqlite3.connect('3.5.tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")

def enter_data():
    c.execute("INSERT INTO example VALUES('Python', '2.7', 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', '3.3', 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Python', '3.4', 'Expert')")
    conn.commit() #Saves the values into the database

def enter_dynamic_data():
    lang = input("What language? ")
    version = float(input("What version? "))
    skill = input("What skill level? ")

    c.execute("INSERT INTO example (Language,Version,Skill) VALUES (?,?,?)", (lang,version,skill))
    #INSERT INTO [table name] [(column headers)]  VALUES ([values]), [(Variables containing values)]
    conn.commit()

def read_from_database():
    sql = "SELECT * FROM example"

    for row in c.execute(sql):
        print(row)
        print(row[0])

def read_from_database_filter():

    what_language = input("What language are we looking for? ")
    what_skill = input("What skill level are we looking for? ")

    sql = "SELECT * FROM example WHERE Language = ? AND Skill == ?"

    for row in c.execute(sql, [(what_language),(what_skill)]):
        print(row)

create_table()

enter_data()

enter_dynamic_data()

read_from_database()

read_from_database_filter()

conn.close()
