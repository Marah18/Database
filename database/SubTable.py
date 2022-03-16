import pandas as pd
import mysql.connector as mysql


mydb = mysql.connect(user = 'root', password = 'MarahAwad11', 
                    host = '127.0.0.1', database='Awad')
cursor = mydb.cursor()

try:
    cursor.execute("CREATE TABLE Subject_table (ID VARCHAR(255) NOT Null,\
        Subject VARCHAR(255) NOT Null,\
        Start_Date VARCHAR(255) NOT Null)")
except:
    pass
# read values from CSV file 
df = pd.read_csv('SubCSV.csv')
df1 = df.fillna(0)
for i, row in df1.iterrows():
    sql = "INSERT INTO Subject_table VALUES (%s, %s ,%s)"
    cursor.execute(sql, tuple(row))
    mydb.commit()


sql = "SELECT ID from Subject_table"
cursor.execute(sql)
myresult = cursor.fetchall()
for x in myresult:
    print(x)
