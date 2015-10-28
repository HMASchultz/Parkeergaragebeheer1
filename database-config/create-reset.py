__author__ = 'Jan'
import pymysql as SQL
conn = SQL.connect(host = 'jancoz.com', port=3306, user='garage_garage', passwd='123456', db='garage_garage')
cur = conn.cursor()
#Creation of the table
def createtable():
    cur.execute("CREATE TABLE Kentekens(ID INT, Kenteken VARCHAR(8), Tijd INT)")
    for i in range(500):
        cur.execute("INSERT INTO Kentekens VALUES (%d, '00-00-00', 0)" % i)
#Resets all values to default
def resettable():
    confirmation = input("Are you sure you want to reset the database? (Y/n)")
    if confirmation == "y":
        for i in range(500):
            cur.execute("UPDATE Kentekens SET Kenteken='00-00-00' WHERE ID=%d" % i)
            cur.execute("UPDATE Kentekens SET Tijd='0' WHERE ID=%d" % i)

choice = input("Do you want to create a table or reset an existant table?\nCreate/Reset: ")
if choice == "reset":
    resettable()
elif choice == "create":
    createtable()
else:
    pass
conn.commit()