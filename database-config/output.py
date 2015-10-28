__author__ = 'Jan'
import pymysql as SQL
from time import gmtime, strftime
conn = SQL.connect(host = 'jancoz.com', port=3306, user='garage_garage', passwd='123456', db='garage_garage')
cur = conn.cursor()
global minuten
while True:
    kenteken = input("Vul nu het kenteken in (00-xxx-0, xx-xx-00): ")
    voorkomt = 1
    if kenteken == "00-00-00":
        kenteken = "null"
    else:
        pass
    try:
        cur.execute("SELECT ID FROM Kentekens WHERE Kenteken = '{0}'".format(kenteken))
        check = (cur.fetchall())[0][0]
    except:
        print("Het kenteken komt niet voor in de database.")
        voorkomt = 0
    finally:
        minuut = int(strftime("%M"))
        uur = int(strftime("%H"))
        minuuttotaal = (uur*60) + minuut
        cur.execute("SELECT Tijd FROM Kentekens WHERE Kenteken = '{0}'".format(check))
        intminuuttotaal = int(minuuttotaal)
        print(cur.fetchall())
        intcurfetch = (cur.fetchall())
        print(int(''.join(map(str,intcurfetch))))

        minuten = intminuuttotaal - intcurfetch
        cur.execute("UPDATE Kentekens SET Kenteken='00-00-00' WHERE ID={0}".format(check))
        print("Fout!")
        if voorkomt == 1:
            print("Uw auto stond %d minuten in de garage," % minuten)
            print("Tot ziens!")
conn.commit()