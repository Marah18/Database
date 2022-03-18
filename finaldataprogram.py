import mysql.connector as mysql
import pandas as pd
import string
from matplotlib.pyplot import acorr
import csv

cnx = mysql.connect(user = 'root', password = 'MarahAwad11', 
                    host = '127.0.0.1')
# cursor is an object in python makes us able to work with database
cursor = cnx.cursor()
# Name for the database
DB_NAME = 'University'

try:
    cursor.execute("create database University")
except:
    pass

# cursor is an object in python makes us able to work with database

try:
    cursor.execute("create database {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))

except:
    inp = input("Press enter to show the main menu: ")


def main_menu():
    print("The main menu:")
    print("1. List all teachers first name with counting how many teachers have same name grouped by teachers ID. ")
    print("2. List what is the average for male and female students.")
    print("3. Enter the name of the subject to get subjects start date")
    print("4. Enter your ID to get subject/s you study ")
    print("5. Enter subject ID to get how many student study given subject?")
    print("6. List all male teachers last name and their age  ")
    print("7. List all female teachers last name and their age  ")
    print("Q. Quiet")


main_menu()
cnx = mysql.connect(user='root', password='MarahAwad11',
                              host='127.0.0.1', database=DB_NAME)
cursor = cnx.cursor()


try:
    cursor.execute("CREATE TABLE Exam (ID VARCHAR(255) NOT Null,\
    Sub_Id VARCHAR(255) NOT Null,\
    Student_ID VARCHAR(255) NOT Null,\
    City VARCHAR(255) NOT Null,\
    Street VARCHAR(255) NOT Null,\
    Date VARCHAR(255) NOT Null)")
except:
    pass
df = pd.read_csv('ExamCSV__1_.csv')
df1 = df.fillna(0)
for i, row in df1.iterrows():
    sql = "INSERT INTO Exam VALUES ( %s ,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    cnx.commit()
try:
    cursor.execute("CREATE TABLE student (ID VARCHAR(255) NOT Null, \
    Email VARCHAR(255) NOT Null,\
    First_Name VARCHAR(255) NOT Null,\
    Last_Name VARCHAR(255) NOT Null,\
    Gender VARCHAR(255) NOT Null,\
    PhoneNumber VARCHAR(255) NOT Null,\
    SubID VARCHAR(255) NOT Null,\
    Age VARCHAR(225) NOT Null)")
except:
    pass
df = pd.read_csv('Student.csv')
df1 = df.fillna(0)
for i, row in df1.iterrows():
    sql = "INSERT INTO student VALUES ( %s ,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    cnx.commit()
try:
    cursor.execute("CREATE TABLE Teachertable (ID VARCHAR(255) NOT Null, \
    First_Name VARCHAR(255) NOT Null,\
    Last_Name VARCHAR(255) NOT Null,\
    Gender VARCHAR(255) NOT Null,\
    Email VARCHAR(255) NOT Null,\
    SubID VARCHAR(255) NOT Null,\
    PhoneNumber VARCHAR(255) NOT Null)")
except:
    pass
df = pd.read_csv('TeacherCSV.csv')
df1 = df.fillna(0)
for i, row in df1.iterrows():
    sql = "INSERT INTO Teachertable VALUES ( %s ,%s,%s,%s,%s,%s, %s)"
    cursor.execute(sql, tuple(row))
    cnx.commit()
try:
    cursor.execute("CREATE TABLE Subject_table (ID VARCHAR(255) NOT Null,\
        Subject VARCHAR(255) NOT Null,\
        Start_Date VARCHAR(255) NOT Null)")
except:
    pass
df = pd.read_csv('SubCSV.csv')
df1 = df.fillna(0)
for i, row in df1.iterrows():
    sql = "INSERT INTO Subject_table VALUES (%s, %s, %s)"
    cursor.execute(sql, tuple(row))
    cnx.commit()


# while query is true the program is running
query = True

while query:
    user_input = int(input("Please choose one option : "))
    if user_input == 1:
        cursor.execute("SELECT COUNT(ID),First_Name FROM Teachertable GROUP BY First_Name")
        names = cursor.fetchall()
        for i in names:
            print(i[0], i[1])

    elif user_input == 2:
        cursor.execute("SELECT AVG(age) from student WHERE gender='Male'")
        age = cursor.fetchall()
        print("Average for male students is ", end=" ")
        for i in age:
            print(str(i[0]))
        cursor.execute("SELECT AVG(age) from student WHERE Gender='Female'")
        agef = cursor.fetchall()
        print("Average for female students is ", end=" ")
        for i in agef:
            print(str(i[0]))

    elif user_input == 3:
        subjectname = input("Enter the name of the subject: ")
        cursor.execute(f'SELECT Start_Date from Subject_table WHERE Subject="{subjectname}"')
        date = cursor.fetchall()
        count = 1
        print("The start date for this subject is:", end=" ")
        for i in date:
            print(str(i[0]))

    elif user_input == 4:
        yourID = int(input("Write your Id: "))
        cursor.execute(f'SELECT Subject_table.Subject '
                        f'from Subject_table Inner join student '
                        f'on Subject_table.ID = student.SubID where student.ID="{yourID}" ')
        students = cursor.fetchall()
        print("The subjects you study are: ")
        for n in students:
            print(str(n[0]))

    elif user_input == 5:
        subjectname = (input("Write subject name: "))
        cursor.execute(f'SELECT Count(student.ID) '
                        f'from Subject_table Inner join student '
                        f'on Subject_table.ID = student.SubID '
                        f'where Subject_table.Subject="{subjectname}" ')
        students = cursor.fetchall()
        print(f'The Number of student study {subjectname} is: ')
        for n in students:
            print(str(n[0]))

    elif user_input == 6:
        try:
            sql = "CREATE VIEW id_VIEW AS SELECT ID, Last_Name  FROM Teachertable WHERE Gender = 'Male'"
            cursor.execute(sql)
        except:
            pass
        sql = "SELECT * FROM id_VIEW"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        print("The first name for all male teachers:")
        print("ID  Last Name")
        for n in myresult:
            print(str(n[0]), "  ", str(n[1]))

    elif user_input == 7:
        try:
            sql = "CREATE VIEW id_aVIEW AS SELECT ID, Last_Name  FROM Teachertable WHERE Gender = 'Female'"
            cursor.execute(sql)
        except:
            pass
        sql = "SELECT * FROM id_aVIEW"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        print("The first name for all female teachers:")
        print("ID  Last Name")
        for n in myresult:
            print(str(n[0]), "  ", str(n[1]))

    keyuser = input("\n" + "Enter Q to exit or any key to go to main menu: ")
    if keyuser == "Q" or keyuser == "q":
        query = False
        print("Thank you for using this program :) ")
    else:
        main_menu()

