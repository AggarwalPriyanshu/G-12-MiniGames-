import time
from csv import *
from random import *
import mysql.connector as mc

con=mc.connect(host="localhost",user="root",passwd="pass")
'''if con.is_connected():
    print("SUCCESSFULLY CONNECTED TO TABLES.")'''
cur=con.cursor()
cur.execute("create database if not exists GAMERS")
cur.execute("use GAMERS")
cur.execute("create table if not exists GAMERS (FIRST_NAME char(30),MIDDLE_NAME char(30),LAST_NAME char(30),PHONE_NUMBER varchar(15),EMAIL_ID varchar(254),PASSWORD varchar(255))")
exist=input("ARE YOU AN EXISTING VISITOR? ('ENTER' FOR YES OR 'ANY OTHER KEY FOLLOWED BY ENTER' FOR NO): ")
print()
def FORGET():
    readfile=open("GAMERS.csv","r")
    rows=reader(readfile)
    rows=list(rows)
    print()
    length=len(rows)
    for i in range (0,length):
        if EMAIL in rows[i] or EMAIL.upper() in rows[i] or EMAIL.lower() in rows[i]:
            row=rows[i]
            FIRST_NAME=row[0]
            MIDDLE_NAME=row[1]
            LAST_NAME=row[2]
            PHONE_NUMBER=int(row[3])
            EMAIL_ID=row[4]
            EMAIL_ID.upper()
            PASSWORD=row[5]
            break
        else:
            FIRST_NAME="ㅤ"
            MIDDLE_NAME="ㅤ"
            LAST_NAME="ㅤ"
            PHONE_NUMBER="ㅤ"
            EMAIL_ID="ㅤ"
            PASSWORD="ㅤ"
    NUMBER=int(input("ENTER YOUR REGISTERED PHONE NUMBER: "))
    while NUMBER!=PHONE_NUMBER:
        print("WRONG PHONE NUMBER.")
        print()
        NUMBER=int(input("ENTER YOUR REGISTERED PHONE NUMBER: "))
    OTP=randint(100000,999999)
    print()
    print("AN OTP HAS BEEN SENT TO YOUR NUMBER.")
    input("PRESS ENTER TO CONTINUE.")
    print()
    print("==============================================")
    print("CONTACTING THE SERVICE PROVIDER...")
    print("TRYING TO AUTOMATICALLY GET THE MESSAGE...")
    print("MESSAGE RECIEVED.")
    print()
    print("YOUR OTP IS",OTP)
    print("==============================================")
    print()
    otp=int(input("ENTER THE OTP: "))
    while otp==OTP:
        print("YOUR PASSWORD IS",PASSWORD)
        print()
        break
    while otp!=OTP:
        print("WRONG OTP.")
        print()
        otp=int(input("ENTER THE OTP AGAIN: "))
        if otp==OTP:
            print("YOUR PASSWORD IS",PASSWORD)
            print()
            break
def infoold():
    global FIRST_NAME
    global MIDDLE_NAME
    global LAST_NAME
    global PHONE_NUMBER
    global EMAIL_ID
    global EMAIL
    global PASSWORD
    try:
            readfile=open("GAMERS.csv","r")
            rows=reader(readfile)
            rows=list(rows)
            EMAIL=input("ENTER YOUR EMAIL ID: ")
            EMAIL=EMAIL.upper()
            length=len(rows)
            for i in range (0,length):
                if EMAIL in rows[i] or EMAIL.upper() in rows[i] or EMAIL.lower() in rows[i]:
                    row=rows[i]
                    FIRST_NAME=row[0]
                    MIDDLE_NAME=row[1]
                    LAST_NAME=row[2]
                    PHONE_NUMBER=int(row[3])
                    EMAIL_ID=row[4]
                    EMAIL_ID.upper()
                    PASSWORD=row[5]
                    break
                else:
                    FIRST_NAME="ㅤ"
                    MIDDLE_NAME="ㅤ"
                    LAST_NAME="ㅤ"
                    PHONE_NUMBER="ㅤ"
                    EMAIL_ID="ㅤ"
                    PASSWORD="ㅤ"
            if EMAIL!=EMAIL_ID or EMAIL.upper()!=EMAIL_ID.upper() or EMAIL.lower()!=EMAIL_ID.lower():
                print()
                print("THIS EMAIL ID DOESNOT EXIST.")
                print()
                ID=input("WANT TO ENTER THE ID AGAIN OR CREATE A NEW ONE? ('ENTER' TO ENTER ID AGAIN OR 'ANY OTHER KEY FOLLOWED BY ENTER' TO CREATE NEW ID): ")
                print()
                if ID=="":
                    infoold()
                else:
                    infonew()
            else:
                print()
                PASS=input("ENTER THE PASSWORD (PRESS 'ENTER' IF YOU HAVE FORGOTTEN PASSWORD): ")
                print()
                while PASS=="":
                    FORGET()
                    PASS=input("ENTER THE PASSWORD (PRESS 'ENTER' IF YOU HAVE FORGOTTEN PASSWORD): ")
                    print()
                while PASS!=PASSWORD and PASS!="":
                    print("WRONG PASSWORD.")
                    print()
                    PASS=input("ENTER THE PASSWORD (PRESS 'ENTER' IF YOU HAVE FORGOTTEN PASSWORD): ")
                    if PASS=="":
                        FORGET()
                        PASS=input("ENTER THE PASSWORD (PRESS 'ENTER' IF YOU HAVE FORGOTTEN PASSWORD): ")
                        print()
                        break
                while PASS==PASSWORD:
                    break
                if MIDDLE_NAME!="":
                    print("YOU ARE SUCCESSFULLY LOGGED IN",FIRST_NAME,MIDDLE_NAME,LAST_NAME)
                elif MIDDLE_NAME=="":
                    print("YOU ARE SUCCESSFULLY LOGGED IN",FIRST_NAME,LAST_NAME)
                readfile.close()
    except FileNotFoundError or FileExistsError:
        input("ENTER YOUR EMAIL ID: ")
        print()
        print("THE PROGRAM COULD NOT FETCH ANY SIMILAR RECORD.")
        print("THIS PROBLEM OCCURS ONLY WHEN YOU ARE A NEW USER.")
        input("PRESS ENTER TO GO TO THE SIGN-UP PAGE.")
        print()
        file=open("GAMERS.csv","a",newline="")
        lst=writer(file)
        details=["FIRST_NAME","MIDDLE_NAME","LAST_NAME","PHONE_NUMBER","EMAIL_ID","PASSWORD"]
        lst.writerow(details)
        file.close()
        infonew()
def infonew():
    file=open("GAMERS.csv","a",newline="")
    lst=writer(file)
    print("SINCE YOU ARE A NEW USER, WE WANT YOUR DETAILS BEFORE WE REDIRECT YOU TO THE GAMES.")
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
    PHONE_NUMBER=int(input("ENTER YOUR PHONE NUMBER: "))
    print()
    while len(str(PHONE_NUMBER))!=10:
        country=input("ARE YOU AN INDIAN? ('ENTER' FOR YES OR 'ANY OTHER KEY FOLLOWED BY ENTER' FOR NO): ")
        if country=="":
            print("THE PHONE NUMBER YOU ENTERED IS INVALID ACCORDING TO INDIAN PHONE DIRECTORIES.")
            PHONE_NUMBER=int(input("ENTER A VALID PHONE NUMBER: "))
            print()
        else:
            print("OK. WE GOT IT.")
            print("YOUR INFORMATION IS STORED.")
            print()
            break
    EMAIL_ID=input("ENTER AN EMAIL ID FOR YOUR ACCOUNT: ")
    print()
    readfile=open("GAMERS.csv","r")
    rows=reader(readfile)
    rows=list(rows)
    length=len(rows)
    for i in range (0,length):
        while EMAIL_ID in rows[i] and "@" in EMAIL_ID and "." in EMAIL_ID:
            print()
            print("THIS EMAIL IS ALREADY IN USE.")
            print("USE SOME OTHER EMAIL ID.")
            print()
            EMAIL_ID=input("ENTER AN EMAIL ID FOR YOUR ACCOUNT: ")
            print()
        while "@" not in EMAIL_ID or "." not in EMAIL_ID:
            print("THIS EMAIL ID IS INVALID.")
            print("THE EMAIL ID MUST CONTAIN A '@' AND A '.'")
            print("EXAMPLE OF VALID EMAIL ID: hello1234@gmail.com")
            print()
            EMAIL_ID=input("ENTER A VALID EMAIL ID FOR YOUR ACCOUNT: ")
            print()
    readfile.close()
    PASSWORD=input("ENTER A PASSWORD FOR YOUR ACCOUNT (MIN 6 DIGITS): ")
    print()
    while len(PASSWORD)<6:
        print("THE LENGTH OF PASSWORD SHOULD BE AT LEAST 6 DIGITS.")
        PASSWORD=input("ENTER A PASSWORD FOR YOUR ACCOUNT (MIN 6 DIGITS): ")
        print()
    details=[FIRST_NAME,MIDDLE_NAME,LAST_NAME,PHONE_NUMBER,EMAIL_ID,PASSWORD]
    insertintosql="insert into GAMERS(FIRST_NAME,MIDDLE_NAME,LAST_NAME,PHONE_NUMBER,EMAIL_ID,PASSWORD) values (%s,%s,%s,%s,%s,%s)"
    tdetails=tuple(details)
    cur.execute(insertintosql,tdetails)
    con.commit()
    lst.writerow(details)
    file.close()
    print("YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY.")
    print("YOU NEED TO LOGIN TO YOUR ACCOUNT TO CONTINUE TO GAMES.")
    print()
    print("OPENING THE LOGIN PAGE.....")
    print("LOGIN PAGE LOADED.")
    print()
    input("PRESS ENTER TO CONTINUE.")
    print()
    infoold()
if exist=="":
    infoold()
else:
    infonew()
print()

