import pandas as pd
import mysql.connector as mysql



mydb = mysql.connect(user = 'root', password = 'MarahAwad11', host = '127.0.0.1', database='Awad')
cursor = mydb.cursor()

try:
    cursor.execute("CREATE TABLE student (ID VARCHAR(255) NOT Null, \
    Email VARCHAR(255) NOT Null,\
    First_Name VARCHAR(255) NOT Null,\
    Last_Name VARCHAR(255) NOT Null,\
    Gender VARCHAR(255) NOT Null,\
    PhoneNumber VARCHAR(255) NOT Null,\
    SubID VARCHAR(255) NOT Null,\
    Age int NOT Null)")
except:
    pass

df = pd.read_csv('Student.csv')
df1 = df.fillna(0)
for i, row in df1.iterrows():
    sql = "INSERT INTO student VALUES (%s, %s ,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    mydb.commit()

sql = "SELECT ID from student"
cursor.execute(sql)
myresult = cursor.fetchall()
for x in myresult:
    print(x)