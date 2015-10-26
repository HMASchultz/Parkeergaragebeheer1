__author__ = 'Jan'
import pymysql as SQL
conn = SQL.connect(host = 'jancoz.com', port=3306, user='garage_garage', passwd='123456', db='garage_garage')
cur = conn.cursor()
input = "0"
input2 = ""
while input != input2 and input != "":
    check = ""
    while check != "00-00-00":
        for i in range(500):
            cur.execute("SELECT Kenteken from Kentekens WHERE ID=0")
            print(i)
            check = (cur.fetchall())[0][0]
            print(check)
    input2 = input