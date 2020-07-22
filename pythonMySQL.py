import mysql.connector

db = mysql.connector.connect(
    host = "localhost", 
    user="",
    passwd="",
    database="pythonMysqldb"
)

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE pythonMysqldb")

#mycursor.execute("CREATE TABLE Language(name VARCHAR(40), year VARCHAR(40), ID int PRIMARY KEY AUTO_INCREMENT)")

#mycursor.execute("INSERT INTO Language (name, year) VALUES (%s, %s)", ("Python 3.8.5", "2020"))
#db.commit()

mycursor.execute("SELECT * FROM Language")

for x in mycursor:
    print(x)
