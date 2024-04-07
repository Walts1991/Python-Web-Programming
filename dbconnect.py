import MySQLdb

def connection():
    conn = MySQLdb.connect(host='localhost',user='root',passwd='',db='Test')
    c = conn.cursor()
    return conn,c

if __name__ == '__main__':
    conn, c = connection()
    print("It worked!")
