__author__ = 'Jan'
import pymysql as SQL
conn = SQL.connect(host = 'jancoz.com', port=3306, user='garage_garage', passwd='123456', db='garage_garage')
cur = conn.cursor()
freespots = 0
for i in range(500):
    cur.execute("SELECT Kenteken from Kentekens WHERE ID=%d" % i)
    check = (cur.fetchall())[0][0]
    if check == "00-00-00":
        freespots += 1
    else:
        pass
print(freespots)