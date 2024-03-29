import sqlite3

conn = sqlite3.connect('3.6.tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")

def enter_data():
    c.execute("INSERT INTO example VALUES('Python', '2.7', 'beginner')")
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

def read_from_database_limit(): #Generally only use limit when updating / deleting data

    sql = "SELECT * FROM example LIMIT 2"

    for row in c.execute(sql):
        print(row)

def update_table():

    sql = "UPDATE example SET Skill = 'Beginner' WHERE skill = 'beginner'"

    c.execute(sql)

    sql = "SELECT * FROM example"

    for row in c.execute(sql):
        print(row)

    conn.commit()

def delete_from_table():
    sql = "SELECT * from example"

    for row in c.execute(sql):
        print(row)

    print(20*"#")

    sql = "DELETE FROM example WHERE Skill = 'Beginner'"

    c.execute(sql)

    conn.commit()

    sql = "SELECT * from example"

    for row in c.execute(sql):
        print(row)

def main():
    create_table()

    enter_data()

    enter_dynamic_data()

    read_from_database()

    read_from_database_limit()

    update_table()

    delete_from_table()

    conn.close()

main()
