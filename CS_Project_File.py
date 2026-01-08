import time
from csv import *
from random import *
import os
import mysql.connector as mc

con=mc.connect(host="localhost",user="root",passwd="pass")
'''if con.is_connected():z
    print("SUCCESSFULLY CONNECTED TO TABLES.")'''
cur=con.cursor()
cur.execute("create database if not exists GAMERS")
cur.execute("use GAMERS")
cur.execute("create table if not exists GAMERS (FIRST_NAME char(30),MIDDLE_NAME char(30),LAST_NAME char(30),PHONE_NUMBER varchar(15),EMAIL_ID varchar(254),PASSWORD varchar(255))")
print("WELCOME TO THIS MINI-GAME PROGRAM CREATED BY ADITYA PANDEY & PRIYANSHU AGGARWAL.")
print("BEFORE WE REDIRECT YOU TO THE GAMES, YOU NEED TO FOLLOW THE FOLLOWING SIMPLE STEPS.")
print()
print("1. YOU WANT TO LOGIN/SIGNUP TO YOUR ACCOUNT.")
print("2. YOU ARE AN ANONYMOUS USER. YOU WANT TO PLAY GAMES WITHOUT ANY ACCOUNT.")
print()
account=int(input("ENTER YOUR CHOICE (1 OR 2): "))
print()
while account>2 or account<1:
    print("INVALID CHOICE.")
    account=int(input("ENTER A VALID CHOICE (1 OR 2): "))
    print()
else:
    if account==1:
        import File_Handling
        FIRST_NAME=File_Handling.FIRST_NAME
        MIDDLE_NAME=File_Handling.MIDDLE_NAME
        LAST_NAME=File_Handling.LAST_NAME
        PHONE_NUMBER=File_Handling.PHONE_NUMBER
        EMAILID=File_Handling.EMAIL_ID
        PASSWORD=File_Handling.PASSWORD
        while True:
            print("THIS IS YOUR ACCOUNT.")
            print("WHAT DO YOU WANT TO DO?")
            print()
            print("1. VIEW ACCOUNT DETAILS.")
            print("2. EDIT ACCOUNT DETAILS.")
            print("3. DELETE ACCOUNT DETAILS.")
            print("4. CONTINUE TO GAMES.")
            print("5. EXIT THE PROGRAM.")
            print()
            accountdetails=int(input("ENTER YOUR CHOICE: "))
            print()
            if accountdetails==1:
                print("FIRST WE NEED TO VERIFY IT IS YOU.")
                checkaccount=input("ENTER YOUR PASSWORD: ")
                while checkaccount!=PASSWORD:
                    print()
                    print("WRONG PASSWORD.")
                    checkaccount=input("ENTER CORRECT PASSWORD: ")
                if checkaccount==PASSWORD:
                    print()
                    print("PASSWORD VERIFIED.")
                    print("HERE ARE YOUR ACCOUNT DETAILS:")
                    print()
                    print("EMAIL ID:",EMAILID)
                    print("PASSWORD:",PASSWORD)
                    print("FIRST NAME:",FIRST_NAME)
                    if MIDDLE_NAME!="":
                        print("MIDDLE NAME:",MIDDLE_NAME)
                    print("LAST NAME:",LAST_NAME)
                    print("PHONE NUMBER:",PHONE_NUMBER)
                    print("\n============================================================\n")
            elif accountdetails==2:
                def changeinprogram():
                    global FIRST_NAME
                    global MIDDLE_NAME
                    global LAST_NAME
                    global PHONE_NUMBER
                    global EMAIL_ID
                    global PASSWORD
                    readfile=open("GAMERS.csv","r")
                    rows=reader(readfile)
                    rows=list(rows)
                    length=len(rows)
                    for i in range (0,length):
                        row=rows[i]
                        if EMAILID in row:
                            FIRST_NAME=row[0]
                            MIDDLE_NAME=row[1]
                            LAST_NAME=row[2]
                            PHONE_NUMBER=int(row[3])
                            EMAIL_ID=row[4]
                            EMAIL_ID.upper()
                            PASSWORD=row[5]
                            break
                        elif EMAILID not in row:
                            FIRST_NAME="ㅤ"
                            MIDDLE_NAME="ㅤ"
                            LAST_NAME="ㅤ"
                            PHONE_NUMBER="ㅤ"
                            EMAIL_ID="ㅤ"
                            PASSWORD="ㅤ"
                    readfile.close()
                print("FIRST WE NEED TO VERIFY ITS YOU.")
                checkaccount=input("ENTER YOUR PASSWORD: ")
                while checkaccount!=PASSWORD:
                    print()
                    print("WRONG PASSWORD.")
                    checkaccount=input("ENTER CORRECT PASSWORD: ")
                if checkaccount==PASSWORD:
                    print()
                    print("PASSWORD VERIFIED.")
                    changeinprogram()
                    def editaccount():
                        global writedata
                        global tempwrite
                        afile=open("GAMERS.csv","r")
                        data=reader(afile)
                        record=[]
                        for i in data:
                            record.append(i)
                        afile.close()
                        tempwrite=open("temp.csv","w",newline="")
                        writedata=writer(tempwrite)
                        for i in record:
                            if i[4]!=EMAILID:
                                writedata.writerow(i)
                    detailschange=int(input("WHICH DETAIL DO YOU WANT TO CHANGE?[NAME(1), PHONE NUMBER(2), PASSWORD(3)]: "))
                    print()
                    if detailschange==1:
                        NEWFIRSTNAME=input("ENTER A NEW FIRST NAME: ")
                        print()
                        while NEWFIRSTNAME=="":
                            print("FIRST NAME CANNOT BE EMPTY.")
                            NEWFIRSTNAME=input("ENTER A NEW FIRST NAME: ")
                            print()
                        NEWMIDDLENAME=input("ENTER A NEW MIDDLE NAME (PRESS 'ENTER' IF YOU DONOT HAVE ONE): ")
                        print()
                        NEWLASTNAME=input("ENTER A NEW LAST NAME: ")
                        print()
                        while NEWLASTNAME=="":
                            print("LAST NAME CANNOT BE EMPTY.")
                            NEWLASTNAME=input("ENTER A NEW LAST NAME: ")
                            print()
                        editaccount()
                        datalst=[NEWFIRSTNAME,NEWMIDDLENAME,NEWLASTNAME,PHONE_NUMBER,EMAIL_ID,PASSWORD]
                        updatetosql="update GAMERS set FIRST_NAME=%s, MIDDLE_NAME=%s, LAST_NAME=%s where EMAIL_ID=%s"
                        cur.execute(updatetosql,(NEWFIRSTNAME,NEWMIDDLENAME,NEWLASTNAME,EMAIL_ID))
                        con.commit()
                        writedata.writerow(datalst)
                        print("CHANGES SUCCESSFULLY DONE.")
                        tempwrite.close()
                        os.remove("GAMERS.csv")
                        os.rename("temp.csv","GAMERS.csv")
                        changeinprogram()
                        print("============================================================")
                        print()
                    elif detailschange==2:
                        NEWPHONENUMBER=input("ENTER A NEW PHONE NUMBER: ")
                        editaccount()
                        datalst=[FIRST_NAME,MIDDLE_NAME,LAST_NAME,NEWPHONENUMBER,EMAIL_ID,PASSWORD]
                        updatetosql="update GAMERS set PHONE_NUMBER=%s where EMAIL_ID=%s"
                        cur.execute(updatetosql,(NEWPHONENUMBER,EMAIL_ID))
                        con.commit()
                        writedata.writerow(datalst)
                        print("CHANGES SUCCESSFULLY DONE.")
                        tempwrite.close()
                        os.remove("GAMERS.csv")
                        os.rename("temp.csv","GAMERS.csv")
                        changeinprogram()
                        print("============================================================")
                        print()
                    elif detailschange==3:
                        NEWPASSWORD=input("ENTER A NEW PASSWORD FOR YOUR ACCOUNT: ")
                        editaccount()
                        datalst=[FIRST_NAME,MIDDLE_NAME,LAST_NAME,PHONE_NUMBER,EMAIL_ID,NEWPASSWORD]
                        updatetosql="update GAMERS set PASSWORD=%s where EMAIL_ID=%s"
                        cur.execute(updatetosql,(NEWPASSWORD,EMAIL_ID))
                        con.commit()
                        writedata.writerow(datalst)
                        print("CHANGES SUCCESSFULLY DONE.")
                        tempwrite.close()
                        os.remove("GAMERS.csv")
                        os.rename("temp.csv","GAMERS.csv")
                        changeinprogram()
                        print("============================================================")
                        print()
                    else:
                        print("INVALID CHOICE.")
                        print("============================================================")
                        print()
            elif accountdetails==3:
                def removalinprogram():
                    global FIRST_NAME
                    global MIDDLE_NAME
                    global LAST_NAME
                    global PHONE_NUMBER
                    global EMAIL_ID
                    global PASSWORD
                    readfile=open("GAMERS.csv","r")
                    rows=reader(readfile)
                    rows=list(rows)
                    length=len(rows)
                    for i in range (0,length):
                        row=rows[i]
                        if EMAILID in row:
                            FIRST_NAME=row[0]
                            MIDDLE_NAME=row[1]
                            LAST_NAME=row[2]
                            PHONE_NUMBER=int(row[3])
                            EMAIL_ID=row[4]
                            EMAIL_ID.upper()
                            PASSWORD=row[5]
                            break
                        elif EMAILID not in row:
                            FIRST_NAME="ㅤ"
                            MIDDLE_NAME="ㅤ"
                            LAST_NAME="ㅤ"
                            PHONE_NUMBER="ㅤ"
                            EMAIL_ID="ㅤ"
                            PASSWORD="ㅤ"
                    readfile.close()
                print("FIRST WE NEED TO VERIFY ITS YOU.")
                checkaccount=input("ENTER YOUR PASSWORD: ")
                while checkaccount!=PASSWORD:
                    print()
                    print("WRONG PASSWORD.")
                    checkaccount=input("ENTER CORRECT PASSWORD: ")
                if checkaccount==PASSWORD:
                    print()
                    print("ACCOUNT DELETED SUCCESSFULLY.")
                    print("THANK YOU FOR USING OUR SERVICES.")
                    removalinprogram()
                    afile=open("GAMERS.csv","r")
                    data=reader(afile)
                    record=[]
                    for i in data:
                        record.append(i)
                    afile.close()
                    tempwrite=open("temp.csv","w",newline="")
                    writedata=writer(tempwrite)
                    for i in record:
                        if i[4]!=EMAILID:
                            writedata.writerow(i)
                    tempwrite.close()
                    os.remove("GAMERS.csv")
                    os.rename("temp.csv","GAMERS.csv")
                    cur.execute("drop table GAMERS")
                    cur.execute("create table GAMERS (FIRST_NAME char(30),MIDDLE_NAME char(30),LAST_NAME char(30),PHONE_NUMBER varchar(15),EMAIL_ID varchar(254),PASSWORD varchar(255))")
                    addlst=[]
                    for x in record:
                        if x[4]!=EMAILID:
                            addlst.append(x)
                    for y in addlst:
                        taddlst=tuple(y)
                        insertintosql="insert into GAMERS(FIRST_NAME,MIDDLE_NAME,LAST_NAME,PHONE_NUMBER,EMAIL_ID,PASSWORD) values (%s,%s,%s,%s,%s,%s)"
                        cur.execute(insertintosql,taddlst)
                        con.commit()
                break
            elif accountdetails==4:
                import Games
                count=Games.count
                print()
                if count==1:
                    if MIDDLE_NAME!="":
                        print("THANK YOU FOR PLAYING THE GAME",FIRST_NAME,MIDDLE_NAME,LAST_NAME)
                    elif MIDDLE_NAME=="":
                        print("THANK YOU FOR PLAYING THE GAME",FIRST_NAME,LAST_NAME)
                if count>1:
                    if MIDDLE_NAME!="":
                        print("THANK YOU FOR PLAYING THE GAMES",FIRST_NAME,MIDDLE_NAME,LAST_NAME)
                    elif MIDDLE_NAME=="":
                        print("THANK YOU FOR PLAYING THE GAMES",FIRST_NAME,LAST_NAME)
                break
            elif accountdetails == 5:
                print("EXITTING THE PROGRAM...")
                time.sleep(3)
                print("THANKS FOR VISITING.")
                break
            else:
                print("INVALID CHOICE.")
                print()
    elif account==2:
        print("BEFORE REDIRECTING YOU TO THE GAMES, WE NEED YOUR FULL NAME.")
        print()
        FIRST_NAME=input("ENTER YOUR FIRST NAME: ")
        print()
        while FIRST_NAME=="":
            print("FIRST NAME CANNOT BE EMPTY.")
            FIRST_NAME=input("ENTER YOUR FIRST NAME: ")
            print()
        MIDDLE_NAME=input("ENTER YOUR MIDDLE NAME (PRESS 'ENTER' IF YOU DONOT HAVE ONE): ")
        print()
        LAST_NAME=input("ENTER YOUR LAST NAME: ")
        print()
        while LAST_NAME=="":
            print("LAST NAME CANNOT BE EMPTY.")
            LAST_NAME=input("ENTER YOUR LAST NAME: ")
            print()
        print("THANK YOU FOR PROVIDING THE DETAILS.")
        print("YOU CAN NOW CONTINUE TO THE GAMES.")
        print()
        import Games
        count=Games.count
        print()
        if count==1:
            if MIDDLE_NAME!="":
                print("THANK YOU FOR PLAYING THE GAME",FIRST_NAME,MIDDLE_NAME,LAST_NAME)
            elif MIDDLE_NAME=="":
                print("THANK YOU FOR PLAYING THE GAME",FIRST_NAME,LAST_NAME)
        if count>1:
            if MIDDLE_NAME!="":
                print("THANK YOU FOR PLAYING THE GAMES",FIRST_NAME,MIDDLE_NAME,LAST_NAME)
            elif MIDDLE_NAME=="":
                print("THANK YOU FOR PLAYING THE GAMES",FIRST_NAME,LAST_NAME)

