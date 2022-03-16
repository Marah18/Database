import pandas as pd
import mysql.connector as mysql

mydb = mysql.connect(user = 'root', password = 'MarahAwad11', 
                    host = '127.0.0.1', database='Awad')
cursor = mydb.cursor()

try:
    cursor.execute("CREATE TABLE Exam (ID VARCHAR(255) NOT Null, \
    Sub_Id VARCHAR(255) NOT Null,\
    Student_ID VARCHAR(255) NOT Null,\
    City VARCHAR(255) NOT Null,\
    Street VARCHAR(255) NOT Null,\
    Date VARCHAR(255) NOT Null)")
except:
    pass
# read values from CSV file
df = pd.read_csv('ExamCSV__1_.csv')
df1 = df.fillna(0)
for i, row in df1.iterrows():
    sql = "INSERT INTO Exam VALUES ( %s ,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    mydb.commit()


sql = "SELECT ID from Exam"
cursor.execute(sql)
myresult = cursor.fetchall()
for x in myresult:
    print(x)
