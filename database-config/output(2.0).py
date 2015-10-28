__author__ = 'Jan'
import pymysql as SQL
from time import gmtime, strftime
conn = SQL.connect(host = 'jancoz.com', port=3306, user='garage_garage', passwd='123456', db='garage_garage')
cur = conn.cursor()
while True:
    kenteken = input("Vul nu het kenteken in (00-xxx-0, xx-xx-00): ")
    cur.execute("SELECT ID FROM Kentekens WHERE Kenteken = '{0}'".format(kenteken))
    try:
        check = cur.fetchall()[0][0]
    except:
        print("Het kenteken komt niet voor in onze database.")
        continue
    minuut = int(strftime("%M"))
    uur = int(strftime("%H"))
    minuuttotaal2 = (uur*60) + minuut
    cur.execute("SELECT Tijd FROM Kentekens WHERE Kenteken = '{0}'".format(kenteken))
    minuuttotaal1 = cur.fetchall()[0][0]
    minutjes = minuuttotaal2 - minuuttotaal1
    cur.execute("UPDATE Kentekens SET Kenteken='00-00-00' WHERE ID={0}".format(check))
    cur.execute("UPDATE Kentekens SET Tijd='0' WHERE ID={0}".format(check))
    print("Uw auto heeft hier {0} minuten gestaan, pay up mwafaka!".format(minutjes))
conn.commit()

