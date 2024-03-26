import sqlite3

conn = sqlite3.connect('3.2.tutorial.db')
c = conn.cursor() #same for MySql - similar to mouse cursor

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)") #All caps for SQL specific syntax / #example = table name
    #[Column name] [DATA TYPE] for column headings
    #VARCHAR = Variable character type - can be used for all types
    #REAL = Similar to float

create_table()

conn.close()
