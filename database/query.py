import string
from matplotlib.pyplot import acorr
import mysql.connector as mysql
import csv


cnx = mysql.connect(user = 'root', password = 'MarahAwad11', 
                    host = '127.0.0.1', database='Awad')
#Name for the database 
DB_Name = 'Student'

#cursor is an object in python makes us able to work with database
acursor = cnx.cursor()

def main_minu():          
    print ("The main menu:")
    print("1. List all teachars first name with counting how many teachers have same name grouped by teachers ID. ")
    print("2. List what is the average for male and female students.")
    print("3. Enter the name of the subject to get subjects start date")
    print("4. Enter your ID to get subject/s you study ")
    print("5. Enter subjct ID to get how many student study given subject?")
    print("6. List all male teachers last name and their age  ")
    print("7. List all female teachers last name and their age  ")
    print("Q. Quiet")
    
main_minu()  
#while query is true the program is running
query = True

while query:    
    user_input = int(input("Please choose one option : "))
    if user_input == 1:
        acursor.execute("SELECT COUNT(ID),First_Name FROM Teachertable GROUP BY First_Name")
        names = acursor.fetchall()
        for i in names:
            print(i[0], i[1])

    elif  user_input == 2:
        acursor.execute ("SELECT AVG(Age) from student WHERE Gender='Male'")
        age = acursor.fetchall()
        print ("Avreage for male students is ", end=" ")
        for i in age:
            print(str(i[0]))                 
        acursor.execute ("SELECT AVG(Age) from student WHERE Gender='Female'")
        agef = acursor.fetchall()
        print ("Avreage for female students is ",end=" ")
        for i in agef:
            print(str(i[0])) 

    elif  user_input == 3:
        subjectname = input("Enter the name of the subject: ")
        acursor.execute (f'SELECT Start_Date from Subject_table WHERE Subject="{subjectname}"')
        date = acursor.fetchall()
        count=1 
        print("The start date for this subject is:", end=" ")
        for i in date:
            print(str(i[0])) 

    elif user_input==4:
        yourID = int(input("Whrite your Id: "))
        acursor.execute(f'SELECT Subject_Table.Subject from Subject_table Inner join student on Subject_table.ID = student.SubID where student.ID="{yourID}" ')
        students = acursor.fetchall()
        print ("The subjects you study are: ")
        for n in students:
            print(str(n[0])) 
        
    elif user_input==5:
        subjectname = (input("Whrite subject name: "))
        acursor.execute(f'SELECT Count(student.ID) from Subject_table Inner join student on Subject_table.ID = student.SubID where Subject_table.Subject="{subjectname}" ')
        students = acursor.fetchall()
        print (f'The Number of student study {subjectname} is: ')
        for n in students:
            print(str(n[0]))     
             
    elif user_input==6:
        try:
            sql = "CREATE VIEW id_VIEW AS SELECT ID, Last_Name  FROM Teachertable WHERE Gender = 'Male'"
            acursor.execute(sql)
        except:
            pass        
        sql = "SELECT * FROM id_VIEW"
        acursor.execute(sql)
        myresult = acursor.fetchall()
        print("The first name for all male teachers:")            
        print("ID  Last Name")            
        for n in myresult:
            print(str(n[0]),"  ", str(n[1]))    
            
    elif user_input==7:
        try:
            sql = "CREATE VIEW id_aVIEW AS SELECT ID, Last_Name  FROM Teachertable WHERE Gender = 'Female'"
            acursor.execute(sql)
        except:
            pass        
        sql = "SELECT * FROM id_aVIEW"
        acursor.execute(sql)
        myresult = acursor.fetchall()
        print("The first name for all female teachers:")            
        print("ID  Last Name")            
        for n in myresult:
            print(str(n[0]),"  ", str(n[1]))  
                        
    keyuser = input("\n"+"Enter Q to exit or any key to go to main menu: ")
    if keyuser == "Q" or keyuser == "q":
        query = False
        print("Thank you for using this program :) ")
    else: 
        main_minu()