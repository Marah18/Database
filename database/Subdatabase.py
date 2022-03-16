import mysql.connector as mysql


mydb = mysql.connect(user = 'root', password = 'MarahAwad11', 
                    host = '127.0.0.1', database='Awad')
cursor = mydb.cursor()
try:
    cursor.execute("create database Subjectdb")
except:
    print("Already Created")
    pass