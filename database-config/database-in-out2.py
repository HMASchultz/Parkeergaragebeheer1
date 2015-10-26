__author__ = 'Jan'
import pymysql as SQL
conn = SQL.connect(host = 'jancoz.com', port=3306, user='garage_garage', passwd='123456', db='garage_garage')
cur = conn.cursor()
#cur.execute("INSERT INTO Safe VALUES(1, 0)")
def createtable():
    #cur.execute("CREATE TABLE Auto (ID INT)")
    cur.execute("INSERT INTO Auto VALUES (1)")
    cur.execute("INSERT INTO Auto VALUES (2)")
    cur.execute("INSERT INTO Auto VALUES (3)")
createtable()
conn.commit()