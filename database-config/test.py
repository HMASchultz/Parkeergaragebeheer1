__author__ = 'Jan'
import pymysql as SQL
conn = SQL.connect(host = 'jancoz.com', port=3306, user='garage_garage', passwd='123456', db='garage_garage')
cur = conn.cursor()
cur.execute("UPDATE Kentekens SET Kenteken='3-APC-72' WHERE ID=1")