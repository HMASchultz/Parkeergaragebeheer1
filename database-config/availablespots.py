__author__ = 'Jan'
import pymysql as SQL
import time
conn = SQL.connect(host = 'jancoz.com', port=3306, user='garage_garage', passwd='123456', db='garage_garage')
cur = conn.cursor()
while True:
    time.sleep(10)
    freespots = 0
    for i in range(500):
        cur.execute("SELECT Kenteken from Kentekens WHERE ID=%d" % i)
        check = (cur.fetchall())[0][0]
        if check == "00-00-00":
            freespots += 1

        else:
            pass
    print(freespots)
conn.commit()