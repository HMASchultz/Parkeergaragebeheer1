__author__ = 'Jan'
import pymysql as SQL
conn = SQL.connect(host = 'jancoz.com', port=3306, user='garage_garage', passwd='123456', db='garage_garage')
cur = conn.cursor()
while True:
    kenteken = input("Voer kenteken in")
    cur.execute("SELECT ID FROM Kentekens WHERE Kenteken = '{0}'".format(kenteken))
    fgts = cur.fetchall()
    if str(fgts) == "()":
        print("Kenteken komt niet voor.")
    else:
        print("Kenteken komt voor.")