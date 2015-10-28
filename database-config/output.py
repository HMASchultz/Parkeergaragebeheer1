__author__ = 'Jan'
import pymysql as SQL
conn = SQL.connect(host = 'jancoz.com', port=3306, user='garage_garage', passwd='123456', db='garage_garage')
cur = conn.cursor()
while True:
    kenteken = input("Vul nu het kenteken in (00-xxx-0, xx-xx-00): ")
    voorkomt = 1
    if kenteken == "00-00-00":
        kenteken = "null"
    else:
        pass
    try:
        cur.execute("SELECT ID FROM Kentekens WHERE Kenteken = '{0}';".format(kenteken))
        check = (cur.fetchall())[0][0]
    except:
        print("Het kenteken komt niet voor in de database.")
        voorkomt = 0
    finally:
        try:
            cur.execute("UPDATE Kentekens SET Kenteken='00-00-00' WHERE ID={0}".format(check))
        except:
            pass
        if voorkomt == 1:
            print("Tot ziens!")
conn.commit()