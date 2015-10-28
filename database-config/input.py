__author__ = 'Jan'
import pymysql as SQL
conn = SQL.connect(host = 'jancoz.com', port=3306, user='garage_garage', passwd='123456', db='garage_garage')
cur = conn.cursor()
kentekenver = 0
kenteken = 1
while True:
    kenteken = input("Vul nu het kenteken in (00-xxx-0): ")
    if kenteken != kentekenver:
        #checken van eerst volgende beschikbare parkeerplaats
        freespotcheck = ""
        check = 0
        while freespotcheck != "00-00-00":
            cur.execute("SELECT Kenteken from Kentekens WHERE ID=%d" % check)
            freespotcheck = (cur.fetchall())[0][0]
            check += 1
        check -= 1
        #gegeven kenteken in de database flikkeren
        cur.execute("UPDATE Kentekens SET Kenteken='{0}' WHERE ID={1}".format(kenteken, check))
        kentekenver = kenteken
    else:
        print("Het kenteken komt reeds voor in de database.")
conn.commit()