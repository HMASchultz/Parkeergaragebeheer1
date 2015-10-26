__author__ = 'Jan'
import pymysql as SQL
conn = SQL.connect(host = 'jancoz.com', port=3306, user='garage_garage', passwd='123456', db='garage_garage')
cur = conn.cursor()
def createtable():
    cur.execute("CREATE TABLE Kentekens(ID INT, Kenteken VARCHAR(8))")
    for i in range(500):
        cur.execute("INSERT INTO Kentekens VALUES (%d, '00-00-00')" % i)
def resettable():
    confirmation = input("Are you sure you want to reset the database? (Y/n)")
    if confirmation == "y":
        for i in range(500):
            cur.execute("UPDATE Kentekens SET Kenteken='00-00-00' WHERE ID=%d" % i)


#cur.execute("UPDATE Kentekens SET Kenteken='12-AV-FA' WHERE ID=0")
cur.execute("SELECT Kenteken from Kentekens WHERE ID=0")
fgts = cur.fetchall()
print(fgts[0][0])
conn.commit()