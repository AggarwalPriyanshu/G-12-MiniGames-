import time
from random import *
# import numpy as np

print("WELCOME TO THE GAME ZONE.")
print("WE HAVE ORGANIZED SEVERAL MINI-GAMES.")
print()
print("WHICH TYPE OF GAME DO YOU WANT TO PLAY?")
print("1. FUN GAMES")
print("2. QUIZ GAME")
print("3. IQ GAME")
print()
MG=int(input("ENTER YOUR CHOICE: "))
count=1
ans=""
SKIP=0
RIGHT=0
WRONG=0
while ans!="n" and ans!="N":
    if MG==1:
        print()
        print("WELCOME TO THE FUN-GAMES SECTION.")
        print("HERE IS A LIST OF THE GAMES YOU CAN PLAY.")
        print()
        print("1. MATHS TRICKS")
        print("2. GUESS THE NUMBER")
        print("3. LUCKY DRAW")
        print("4. PRANK CALCULATOR")
        print("5. RIDDLES")
        print("6. STONE-PAPER-SCISSORS")
        print()
        mg=int(input("WHICH FUN-GAME DO YOU WANT TO PLAY? ENTER YOUR CHOICE (1,2,3,4,5,6): "))
        if mg==1:
            print()
            print("THIS IS A SIMPLE MATHEMATICS BASED MIND-READING GAME.")
            print()
            print("LOADING RULES.....")
            time.sleep(1.5)
            print()
            print("RULES ARE VERY SIMPLE:")
            print("1. FOLLOW THE INSTRUCTIONS WHICH ARE SHOWN TO YOU ON THE SCREEN.")
            print("2. AFTER YOU HAVE DONE ALL YOUR CALCULATIONS, ENTER YOUR FINAL RESULT WHEN ASKED.")
            print("3. IF YOU HAVE DONE EACH AND EVERY STEP UPTO NOW CORRECTLY, THEN THE COMPUTER WILL DISPLAY THE NUMBER YOU HAD ORIGINALLY CHOSEN.")
            print()
            print("PLEASE NOTE THAT PLEASE DO NOT USE ENTER KEY UNTIL NOT SAID OR YOU WILL DESTROY THE CONTINUITY OF THE PROGRAM.")
            print()
            print("LET'S START THE GAME.")
            input("PRESS ENTER TO CONTINUE.")
            print()
            print("THE GAME IS LOADING.....")
            print("PLEASE WAIT.....")
            time.sleep(5)
            print()
            print(r"1. CHOOSE ANY WHOLE NUMBER.")
            input(r"eg. I CHOOSE '12345'.")
            print()
            print(r"2. ADD 1 TO THE THOUSAND'S PLACE.")
            input(r"eg. '2' IS THE THOUSAND'S PLACE DIGIT IN 12345. SO I DO '2+1'. SO, THE ANSWER IS 13345.")
            print()
            print(r"3. ADD 5 TO THE TEN'S PLACE IN THE RESULTING NUMBER.")
            input(r"eg. '4' IS THE TEN'S PLACE DIGIT IN 13345. SO I DO '4+5'. SO, THE ANSWER IS 13395.")
            print()
            print(r"4. SUBTRACT 8 FROM THE HUNDRED'S PLACE IN THE RESULTING NUMBER.")
            input(r"eg. '3' IS THE HUNDRED'S PLACE DIGIT IN 13395. SO I DO '3-8'. SO THE ANSWER IS 12595.")
            print()
            x=int(input("INPUT YOUR FINAL RESULT HERE: "))
            a=x-250
            print()
            print("ANALYZING THE RESULT AND FETCHING THE ORIGINAL NUMBER.....")
            time.sleep(2)
            if a<0:
                print("I TOLD YOU TO TAKE A POSITIVE NUMBER.")
                print("GO AND STUDY MATHEMATICS.")
            else:
                print("THIS MIGHT TAKE A FEW SECONDS.....")
                time.sleep(1.5)
                print("PLEASE BE PATIENT FOR A WHILE.....")
                time.sleep(5)
                print()
                print("THE NUMBER YOU ORIGINALLY THOUGHT OF IS:",a)
                print()
                f=input(r"AM I RIGHT OR NOT? ['ENTER' FOR YES AND ANY OTHER KEY FOR NO]: ")
                print()
                if f=="":
                    print("I KNOW THE ANSWER WAS RIGHT. I AM A GENIUS.")
                else:
                    print("I AM VERY SORRY TO INFORM YOU THAT YOU ARE VERY WEAK AT MATHEMATICS. GO AND CLEAR YOUR CONCEPTS AND IMPROVE YOUR CALCULATIONS.")

        elif mg==2:
            print()
            print("WHICH TYPE OF GAME YOU WANT TO PLAY-")
            print()
            print("1. SINGLE PLAYER")
            print("2. MULTI PLAYER")
            print()
            GUESS=int(input("ENTER 1 FOR SINGLE PLAYER AND 2 FOR MULTI PLAYER: "))
            while GUESS!=1 and GUESS!=2:
                print()
                print("INVALID CHOICE")
                GUESS=int(input("ENTER 1 FOR SINGLE PLAYER AND 2 FOR MULTI PLAYER: "))
            print()
            if GUESS==1:
                print("GUESS THE NUMBER IS A NUMBER GUESSING GAME.")
                print()
                print("HOW TO PLAY:")
                print()
                print("YOU HAVE TO GUESS THE NUMBER WHICH IS CHOSEN BY THE COMPUTER.")
                print("YOU WILL BE TOLD AFTER EACH ANSWER THAT THE NUMBER CHOSEN BY THE COMPUTER IS HIGHER OR LESSER.")
                print()
                A=randint(1,100)
                print()
                print("THE COMPUTER HAS CHOSEN THE NUMBER.")
                print()
                X1=0
                C1=0
                T=10
                while T>0:
                    C1+=1
                    Y=int(input("GUESS THE NUMBER (BETWEEN 1 AND 100): "))
                    if Y<A:
                        print("HIGHER!")
                        print()
                        T-=1
                    if Y>A:
                        print("LOWER!")
                        print()
                        T-=1
                    if Y==A:
                        print()
                        print("CONGRATULATIONS YOU GOT THE RIGHT ANSWER.")
                        T-=1
                        break
            elif GUESS==2:
                print("GUESS THE NUMBER IS A NUMBER GUESSING GAME.")
                print()
                print("HOW TO PLAY:")
                print()
                print("YOU HAVE TO GUESS THE NUMBER WHICH IS CHOSEN BY THE COMPUTER.")
                print("YOU WILL BE TOLD AFTER EACH ANSWER THAT THE NUMBER CHOSEN BY THE COMPUTER IS HIGHER OR LESSER.")
                print()
                A=randint(1,100)
                PLAYER1=input("PLAYER1 (NAME): ")
                PLAYER2=input("PLAYER2 (NAME): ")
                print()
                print("THE COMPUTER HAS CHOSEN THE NUMBER.")
                print()
                print(PLAYER1,"YOUR TURN NOW.")
                print()
                X1=0
                C1=0
                while X1!=A:
                    C1+=1
                    Y=int(input("GUESS THE NUMBER (BETWEEN 1 AND 100): "))
                    if Y<A:
                        print("HIGHER!")
                        print()
                    if Y>A:
                        print("LOWER!")
                        print()
                    if Y==A:
                        print()
                        print("CONGRATULATIONS YOU GOT THE RIGHT ANSWER.")
                        break
                print()
                print(PLAYER2,"YOUR TURN NOW.")
                print()
                C2=0
                X2=0
                B=randint(1,100)

                while X2!=B:
                    C2+=1
                    Z=int(input("GUESS THE NUMBER (BETWEEN 1 AND 100): "))
                    if Z<B:
                        print("HIGHER!")
                        print()
                    if Z>B:
                        print("LOWER!")
                        print()
                    if Z==B:
                        print()
                        print("CONGRATULATIONS YOU GOT THE RIGHT ANSWER.")
                        break
                if C1<C2:
                    print()
                    print(PLAYER1,"HAS TRIED",C1,"TIMES TO GUESS THE NUMBER.")
                    print()
                    print(PLAYER2,"HAS TRIED",C2,"TIMES TO GUESS THE NUMBER.")
                    print()
                    print("SO",PLAYER1,"HAS WON THE MATCH AND",PLAYER2,"HAS LOST THE MATCH.")
                if C1==C2:
                    print()
                    print(PLAYER1,"HAS TRIED",C1,"TIMES TO GUESS THE NUMBER.")
                    print()
                    print(PLAYER2,"HAS TRIED",C2,"TIMES TO GUESS THE NUMBER.")
                    print()
                    print("SO THE MATCH IS DRAW NOW BETWEEN",PLAYER1,"AND",PLAYER2)
                if C1>C2:
                    print()
                    print(PLAYER1,"HAS TRIED",C1,"TIMES TO GUESS THE NUMBER.")
                    print()
                    print(PLAYER2,"HAS TRIED",C2,"TIMES TO GUESS THE NUMBER.")
                    print()
                    print("SO",PLAYER2,"HAS WON THE MATCH AND",PLAYER1,"HAS LOST THE MATCH.")

        elif mg==3:
            print()
            A=int(input("ENTER A NUMBER FROM 0 TO 9: "))
            while A>=10 or A<0:
                print("YOU WERE SUPPOSED TO ENTER A NUMBER FROM 0 TO 9.")
                print("ENTER A NUMBER AGAIN.")
                print()
                A=int(input("ENTER A NUMBER FROM 0 TO 9: "))
            print()
            B=randint(0,9)
            C=randint(0,9)
            D=randint(0,9)
            while B==C or C==D or D==B:
                B=randint(0,9)
                C=randint(0,9)
                D=randint(0,9)
            else:
                print("LET'S CHECK WHERE YOU LIE IN THE WORLD.")
                print("IN THE LUCKY PHASE...")
                print("OR IN THE UNLUCKY PHASE.")
                print()
                input("PRESS ENTER TO START.")
                print()
                print("THE COMPUTER IS RANDOMLY GENERATING 3 NUMBERS.")
                print("LOADING...")
                print("LOADING COMPLETED.")
                print()
                input("PRESS ENTER FOR YOUR RESULT.")
                print()
                print("1.",B)
                print("2.",C)
                print("3.",D)
                print()
                if A!=B and A!=C and A!=D and B!=C and B!=D and C!=D:
                    print("I HAVE NOT SEEN THIS MUCH UNLUCKY PERSON IN MY WHOLE LIFE.")
                else:
                    print("DON'T BE THIS MUCH HAPPY AS YOU ARE NOT THE ONLY LUCKY PERSON IN THE WORLD.")

        elif mg==4:
            print()
            def f1():
                a=float(input("ENTER FIRST NUMBER: "))
                b=float(input("ENTER SECOND NUMBER: "))
                o=input("ENTER THE OPERATOR FOR OPERATION(+,-,*,/): ")
                print()
                input("PRESS ENTER TO START PROCESSING OF ANSWER.")
                print()
                print("LOADING......")
                print("PROCESSING YOUR ANSWER......")
                print("ANSWER IS ALMOST READY......")
                print("ANSWER IS READY TO BE DISPLAYED.")
                print()
                q=input("PLEASE PRESS ENTER TO SEE THE RESULT.")
                print()
                if q==" ":
                    if o=="+":
                        if a+b==int(a+b):
                            print("THE REQUIRED RESULT IS:",int(a+b))
                        else:
                            print("THE REQUIRED RESULT IS:",a+b)
                    if o=="-":
                        if a-b==int(a-b):
                            print("THE REQUIRED RESULT IS:",int(a-b))
                        else:
                            print("THE REQUIRED RESULT IS:",a-b)
                    if o=="*":
                        if a*b==int(a*b):
                            print("THE REQUIRED RESULT IS:",int(a*b))
                        else:
                            print("THE REQUIRED RESULT IS:",a*b)
                    if o=="/":
                        if a/b==int(a/b):
                            print("THE REQUIRED RESULT IS:",int(a/b))
                        else:
                            print("THE REQUIRED RESULT IS:",a/b)
                else:
                    print("I AM NOT YOUR SERVANT. FOLLOW MY INSTRUCTIONS OR USE REAL CALCULATOR FOR CALCULATION.")
            print("THIS IS A CALCULATOR.")
            print("IT IS USED TO PERFORM ADDITION, SUBTRACTION, MULTIPLICATION AND DIVISION.")
            x=input("WANT A TUTORIAL ON HOW TO USE THE CALCULATOR OR YOU THINK YOU KNOW HOW TO USE CALCULATOR? ('ENTER' FOR TUTORIAL OR 'ANY OTHER KEY FOLLOWED BY ENTER' FOR CALCULATOR): ")
            print()
            if x=="":
                input("TUTORIAL LOADED. PRESS ENTER TO CONTINUE.")
                print()
                print("THIS IS THE TUTORIAL FOR THIS CALCULATOR.")
                print("LIKE EVERY OTHER NORMAL CALCULATOR, THIS CALCULATOR ALSO PERFORMS CALCULATIONS BUT IN A SLIGHT DIFFERENT WAY.")
                print("BECAUSE THIS IS A PRANK CALCULATOR.")
                print("ENTER FIRST NUMBER AND THEN THE SECOND NUMBER.")
                print("ENTER THE OPERATOR FOR THE OPERATION.")
                print("THEN PRESS ENTER FOR THE PROCESSING OF THE CALCULATION.")
                print("THEN AFTER THE ANSWER IS PROCESSED, PRESS SPACEBAR AND THEN PRESS ENTER TO GET THE ANSWER DISPLAYED.")
                print()
                input("PRESS ENTER TO CONTINUE.")
                print()
                f1()
            elif x!="":
                f1()

        elif mg==5:
            print()
            N=randint(0,29)
            P={"What has to be broken before you can use it?":"EGG","I’m tall when I’m young, and I’m short when I’m old. What am I?":"CANDLE"," What is full of holes but still holds water?":"SPONGE","What gets wet while drying?":"TOWEL"," I have branches, but no fruit, trunk or leaves. What am I?":"BANK","What has many keys but can’t open a single lock?":"PIANO"," What can you hold in your left hand but not in your right?":"RIGHT HAND","There’s a one-story house in which everything is yellow. Yellow walls, yellow doors, yellow furniture. What color are the stairs?":"ZERO","I’m light as a feather, yet the strongest person can’t hold me for five minutes. What am I?":"BREATH","It belongs to you, but other people use it more than you do. What is it?":"YOUR NAME","What has words, but never speaks?":"BOOK","What has a head and a tail but no body?":"COIN","What building has the most stories?":"LIBRARY","What has 13 hearts, but no other organs?":"DECK OF CARDS","I am an odd number. Take away a letter and I become even. What number am I?":"SEVEN","If two’s company, and three’s a crowd, what are four and five?":"NINE","Which is heavier: a ton of bricks or a ton of feathers?":"NEITHER","The day before yesterday I was 21, and next year I will be 24. When is my birthday?":"31 DECEMBER","The day before yesterday I was 21, and next year I will be 24. What is the date today?":"1 JANUARY","A man describes his daughters, saying, “They are all blonde, but two; all brunette but two; and all redheaded but two.” How many daughters does he have?":"THREE","If there are three apples and you take away two, how many apples do you have?":"TWO","What begins with an “e” and only contains one letter?":"ENVELOPE","What is found in the middle of Earth?":"R","What word is pronounced the same if you take away its last four letters?":"QUEUE","What is so fragile that saying its name breaks it?":"SILENCE","What can fill a room but takes up no space?":"LIGHT","If you drop me I’m sure to crack, but give me a smile and I’ll always smile back. What am I?":"MIRROR","What goes through cities and fields, but never moves?":"ROAD","I am always hungry and will die if not fed, but whatever I touch will soon turn red. What am I?":"FIRE","What does man love more than life, hate more than death or mortal strife; that which contented men desire; the poor have, the rich require; the miser spends, the spendthrift saves, and all men carry to their graves?":"NOTHING"}
            Q=list(P.keys())
            print(Q[N])
            A=list(P.values())
            INPUT=input("YOUR ANSWER (OR ENTER TO SKIP): ")
            INPUT=INPUT.upper()
            print()
            if INPUT=="":
                print("YOU SKIPPED THE RIDDLE.")
                print("ADMIT IT THAT YOU HAVE NO GUTS TO ATTEMPT THIS RIDDLE.")
                print("THE ANSWER IS: ",A[N])
            elif INPUT==A[N] or INPUT==A[N].lower() or INPUT==A[N].upper():
                print("YOU GOT THE RIGHT ANSWER.")
                print("VERY NICE.")
            else:
                print("SORRY! YOU GOT THE WRONG ANSWER.")
                print("CORRECT ANSWER IS: ",A[N])

        elif mg==6:
            print()
            print("STONE-PAPER-SCISSOR")
            print("RULES ARE SIMPLE. STONE DEFEATS SCISSOR. SCISSOR DEFEAT PAPER. PAPER DEFEATS STONE.")
            SPStry = int(input("ENTER HOW MANY NUMBER OF TRIES YOU WANT: "))
            #SPSlst = ["STONE","PAPER","SCISSOR"]
            SPSi = 0
            SPScmpscr = 0
            SPSusrscr = 0
            while SPSi < SPStry:
                SPS = randint(1,3)
                SPSchc = int(input("\n1. STONE\n2. PAPER\n3. SCISSOR\n\nENTER YOUR CHOICE: "))
                print("COMPUTER HAS CHOSEN.")
                print("YOUR TURN NOW.")


                if SPS == 1:
                    print("COMPUTER CHOSE STONE")
                    if SPSchc == 1:
                        print("IT IS A TIE.")
                    elif SPSchc == 2:
                        print("COMPUTER GOT A POINT.")
                        SPSi += 1
                        SPScmpscr += 1
                    elif SPSchc == 3:
                        print("YOU GOT A POINT.")
                        SPSi += 1
                        SPSusrscr += 1


                if SPS == 2:
                    print("COMPUTER CHOSE PAPER")
                    if SPSchc == 1:
                        print("COMPUTER GOT A POINT.")
                        SPSi += 1
                        SPScmpscr += 1
                    elif SPSchc == 2:
                        print("IT IS A TIE.")
                    elif SPSchc == 3:
                        print("YOU GOT A POINT.")
                        SPSi += 1
                        SPSusrscr += 1


                if SPS == 3:
                    print("COMPUTER CHOSE SCISSOR")
                    if SPSchc == 1:
                        print("YOU GOT A POINT.")
                        SPSi += 1
                        SPSusrscr += 1
                    elif SPSchc == 2:
                        print("COMPUTER GOT A POINT.")
                        SPSi += 1
                        SPScmpscr += 1
                    elif SPSchc == 3:
                        print("IT IS A TIE.")


            print()
            print("THE FINAL SCORES ARE: ")
            print("USER: ",SPSusrscr)
            print("COMPUTER: ",SPScmpscr)
            if SPSusrscr > SPScmpscr:
                print("USER WON.")
            elif SPSusrscr < SPScmpscr:
                print("COMPUTER WON.")
            else:
                print("IT IS A TIE.")
        
        else:
            print("INVALID VALUE TAKEN.")
            print()
            while mg!=1 and mg!=2 and mg!=3 and mg!=4 and mg!=5:
                print("TRY AGAIN!")
                mg=1
            continue
        
        print()
        ans=input("DO YOU WANT TO CONTINUE? ('ENTER' FOR YES OR 'ANY OTHER KEY FOLLOWED BY ENTER' FOR NO): ")
        if ans=="":
            print()
            count+=1
            MG=int(input("WHICH TYPE OF GAME DO YOU WANT TO PLAY?\n\n1. FUN GAMES\n2. MIND GAME\n3. IQ GAME\n\nENTER YOUR CHOICE: "))
        else:
            break

    elif MG==2:
        print()
        print("WELCOME TO THE MIND GAME.")
        print("HERE IS A QUIZ (A KNOWLEDGE TEST) WHICH HAS 5 DIFFERENT SUBJECTS TO CHOOSE.")
        print()
        print("SUBJECTS OF QUIZ:")
        print("1. TECHNOLOGY")
        print("2. ASTRONOMY")
        print("3. NATURE")
        print("4. SPORTS")
        print("5. HISTORY")
        print()
        def f():
            global LEN
            global C
            global NUM
            NUM=int(input("ENTER HOW MANY QUESTIONS WANT TO ATTEMPT(MAXIMUM 20): "))
            print()
            Q=list(SUB.keys())
            A=list(SUB.values())
            for i in range(NUM):
                LIM=randint(0,LEN)
                print(Q[LIM])
                INPUT=input("YOUR ANSWER (OR ENTER TO SKIP): ")
                INPUT=INPUT.upper()
                print()
                if INPUT=="":
                    print("YOU SKIPPED THE QUESTION.")
                    print("ADMIT IT THAT YOU HAVE NO GUTS TO ATTEMPT THIS QUESTION.")
                    print("THE ANSWER IS: ",A[LIM])
                    print()
                elif INPUT==A[LIM] or INPUT==A[LIM].lower() or INPUT==A[LIM].upper():
                    print("YOU GOT THE RIGHT ANSWER.")
                    print("VERY NICE.")
                    print()
                    C+=1
                else:
                    print("SORRY! YOU GOT THE WRONG ANSWER.")
                    print("CORRECT ANSWER IS: ",A[LIM])
                    print()
                del Q[LIM]
                del A[LIM]
                LEN-=1
        SUBJECT=int(input("ENTER YOUR SUBJECT ON WHICH YOU WANT TO GIVE QUIZ: "))
        print()
        C=0
        LEN=19
        if SUBJECT==1:
            SUB={"IN WHICH DECADE WAS THE AMERICAN INSTITUTE OF ELECTRICAL ENGINEERS (AIEE) FOUNDED?\n(A) 1850S\n(B) 1880S\n(C) 1930S\n(D) 1950S":"B","WHAT IS PART OF A DATABASE THAT HOLDS ONLY ONE TYPE OF INFORMATION?\n(A) REPORT\n(B) FIELD\n(C) RECORD\n(D) FILE":"B","IN WHICH DECADE WITH THE FIRST TRANSATLANTIC RADIO BROADCAST OCCUR?\n(A) 1850S\n(B) 1860S\n(C) 1870S\n(D) 1900S":"D","IN WHICH DECADE WAS THE SPICE SIMULATOR INTRODUCED?\n(A) 1950S\n(B) 1960S\n(C) 1970S\n(D) 1980S":"C","MOST MODERN TV'S DRAW POWER EVEN IF TURNED OFF. THE CIRCUIT THE POWER IS USED IN DOES WHAT FUNCTION?\n(A) SOUND\n(B) REMOTE CONTROL\n(C) COLOR BALANCE\n(D)HIGH VOLTAGE":"B","THE PURPOSE OF CHOKE IN TUBE LIGHT IS?\n(A) TO DECREASE THE CURRENT\n(B) TO INCREASE THE CURRENT\n(C) TO DECREASE THE VOLTAGE MOMENTARILY\n(D) TO INCREASE THE VOLTAGE MOMENTARILY":"D","WHO IS LARGELY RESPONSIBLE FOR BREAKING THE GERMAN ENIGMA CODES, CREATED A TEST THAT PROVIDED A FOUNDATION FOR ARTIFICIAL INTELLIGENCE?\n(A) ALAN TURING\n(B) JEFF BEZOS\n(C) GEORGE BOOLE\n(D) CHARLES BABBAGE":"A","WHO DEVELOPED YAHOO?\n(A) DENNIS RITCHIE & KEN THOMPSON\n(B) DAVID FILO & JERRY YANG\n(C) VINT CERF & ROBERT KAHN\n(D) STEVE CASE & JEFF BEZOS":"B","MADE FROM A VARIETY OF MATERIALS, SUCH AS CARBON, WHICH INHIBITS THE FLOW OF CURRENT?\n(A) CHOKE\n(B) INDUCTOR\n(C) RESISTOR\n(D) CAPACITOR":"C","THE MOST COMMON FORMAT FOR A HOME VIDEO RECORDER IS VHS. VHS STANDS FOR?\n(A) VIDEO HOME SYSTEM\n(B) VERY HIGH SPEED\n(C) VIDEO HORIZONTAL STANDARD\n(D) VOLTAGE HOUSE STANDARD":"A","WHAT DOES VVVF STAND FOR?\n(A) VARIANT VOLTAGE VILE FREQUENCY\n(B) VARIABLE VELOCITY VARIABLE FUN\n(C) VERY VERY VICIOUS FREQUENCY\n(D) VARIABLE VOLTAGE VARIABLE FREQUENCY":"D","WHAT FREQUENCY RANGE IS THE HIGH FREQUENCY BAND?\n(A) 100 KHZ\n(B) 1 GHZ\n(C) 30 TO 300 MHZ\n(D) 3 TO 30 MHZ":"D","THE FIRST STEP TO GETTING OUTPUT FROM A LASER IS TO EXCITE AN ACTIVE MEDIUM. WHAT IS THIS PROCESS CALLED?\n(A) PUMPING\n(B) EXCITING\n(C) PRIMING\n(D) RAISING":"A","WHICH MOTOR IS NOT SUITABLE FOR USE AS A DC MACHINE?\n(A) PERMANENT MAGNET MOTOR\n(B) SERIES MOTOR\n(C) SQUIRREL CAGE MOTOR\n(D) SYNCHRONOUS MOTOR":"C","IN WHICH YEAR WAS MIDI(MUSICAL INSTRUMENT DIGITAL INTERFACE) INTRODUCED?\n(A) 1987\n(B) 1983\n(C) 1973\n(D) 1977":"B","WHO CREATED PRETTY GOOD PRIVACY (PGP)?\n(A) PHILIP ZIMMERMANN\n(B) TIM BERNERS-LEE\n(C) MARC ANDREESSEN\n(D) KEN THOMPSON":"A","AFTER THE FIRST PHOTONS OF LIGHT ARE PRODUCED, WHICH PROCESS IS RESPONSIBLE FOR AMPLIFICATION OF THE LIGHT?\n(A) BLACKBODY RADIATION\n(B) STIMULATED EMISSION\n(C) PLANCK'S RADIATION\n(D) EINSTEIN OSCILLATION":"B","IN THE UK, WHAT TYPE OF INSTALLATION REQUIRES A FIREMAN'S SWITCH?\n(A) NEON LIGHTING\n(B) HIGH PRESSURE SODIUM LIGHTING\n(C) WATER FEATURES\n(D) HOTEL ROOMS":"A","IN A COLOR TELEVISION SET USING A PICTURE TUBE A HIGH VOLTAGE IS USED TO ACCELERATE ELECTRON BEAMS TO LIGHT THE SCREEN. WHAT IS THAT VOLTAGE?\n(A) 500 VOLT\n(B) 5000 VOLT\n(C) 25000 VOLT\n(D) 100000 VOLT":"C","WHICH OF THE FOLLOWING CONSISTS OF TWO PLATES SEPARATED BY A DIELECTRIC AND CAN STORE A CHARGE?\n(A) INDUCTOR\n(B) CAPACITOR\n(C) TRANSISTOR\n(D) RELAY":"B"}
            f()
        elif SUBJECT==2:
            SUB={"WHICH IS THE COLDEST PLANET IN THE SOLAR SYSTEM?\n(A)URANUS\n(B)PLUTO\n(C)NEPTUNE\n(D)SATURN":"C","BIG CRUNCH THEORY IS WHICH TO WHICH ERA OF UNIVERSE?\n(A)BIRTH\n(B)DEATH OF UNIVERSE\n(C)HALF LIFE\n(D)NOT RELATED TO UNIVERSE":"B","WHICH CELESTIAL BODIES HAVE TAILS?\n(A)COMETS\n(B)METEROIDS\n(C)STARS\n(D)ASTEROIDS":"A","WHO WAS THE FIRST PERSON TO REACH MOON?\n(A)YURI GAGRIN\n(B)RAKESH SHARMA\n(C)EDMUND HILLARY\n(D)NEIL ARMSTRONG":"D","WHAT IS THE APPROXIMATE DISTANCE BETWEEN EARTH AND SUN?\n(A)1 LIGHT YEAR\n(B)150 MILLION KM\n(C)150 LIGHT YEARS\n(D)1 MILLION KM":"B","WHAT IS THE NAME OF THE ONLY MOON(NATURAL SATELLITE) OF THE EARTH?\n(A)LUNA\n(B)HD189733B\n(C)CORONA\n(D)AURORA":"A","WHICH OF THE FOLLOWING IS NOT A DWARF PLANET?\n(A)HAUMEA\n(B)CERES\n(C)MAKEMAKE\n(D)DYSOMIA":"D","HOW OLD IS THE MOON?\n(A)8 BILLION YEARS\n(B)6.5 BILLION YEARS\n(C)4.5 BILLION YEARS\n(D)3 BILLION YEARS":"C","WHICH IS THE LARGEST SATELLITE OF THE SOLAR SYSTEM?\n(A)GANYMEDE\n(B)EUROPA\n(C)PHOBOS\n(D)KERBEROS":"A","WHERE DO COMETS COME FROM?\n(A)OORT CLOUD\n(B)OUTER SOLAR SYSTEM\n(C)BOTH OF THE ABOVE\n(D)NONE OF THE ABOVE":"A","WHO PROPOSED THE HELOICENTRIC THEORY?\n(A)PTOLMEY\n(B)NEWTON\n(C)KEPLER\n(D)COPERNICUS":"A","AFTER WHOM IS THE PLANET VENUS NAMED?\n(A)APHRODITE\n(B)TERRA\n(C)HERMES\n(D)POSEIDON":"C","WHAT IS THE VISIBLE PATH OF THE METEOROID THAT ENTER'S EARTH ATMOSPHERE CALLED?\n(A)METEOR\n(B)METEORITE\n(C)AURORA\n(D)ALL OF THE ABOVE":"A","WHICH IS THE CLOSEST COMET TO THE EARTH?\n(A)HALLEY'S COMET\n(B)COMET HALE BOPP\n(C)SHOEMAKER LAVY\n(D)LEXELL":"B","WHO WAS THE FIRST PERSON TO PERFORM SPACEWALK?\n(A)EDWARD WHITE\n(B)ALEXI LEONOV\n(C)NEIL ARMSTRONG\n(D)YURI GAGRIN":"B","WHICH WAS THE FIRST MAN-MADE OBJECT TO LAND ON EARTH'S MOON?\n(A)LUNA-3\n(B)LUNA-4\n(C)LUNA-9\n(D)LUNA-10":"C","WHO MADE THE FIRST TRUE ASTRONOMICAL TELESCOPE?\n(A)LIPPERSHEY\n(B)NEWTON\n(C)GALILEO\n(D)KEPLER":"C","WHEN WAS THE SKYLAB SPACE-STATION LAUNCHED?\n(A)1971\n(B)1972\n(C)1978\n(D)1979":"A","WHEN WAS THE NASA ESTABLISHED?\n(A)1955\n(B)1957\n(C)1958\n(D)1959":"C","WHICH OF THESE IS NOT THE MISSION,DIRECTORATES OF NASA?\n(A)AERONAUTICS\n(B)HUMAN EXPLORATION\n(C)SCIENCE\n(D)SPACE EXPLORATION":"D"}
            f()
        elif SUBJECT==3:
            SUB={"WHICH OF THE FOLLOWING IS NOT A CORRECT MATCH?\n(A)SHARK BAY – AUSTRALIA\n(B)CARRASCO NATIONAL PARK – BOLIVIA\n(C)ATLANTIC FOREST SOUTH-EAST RESERVES – FRANCE\n(D)KAKADU NATIONAL PARK – AUSTRALIA":"C","THE INDRAVATI NATIONAL PARK (INP) IS LOCATED IN WHICH STATE?\n(A)CHHATTISGARH\n(B)KARNATAKA\n(C)PUNJAB\n(D)ASSAM":"A","WHAT IS THE DIRECTION OF FLOW OF ENERGY IN AN ECOSYSTEM?\n(A)UNIDIRECTIONAL\n(B)BIDIRECTIONAL\n(C)MULTIDIRECTIONAL\n(D)CYCLIC":"A","THE ADICHUNCHANAGIRI WILDLIFE SANCTUARY (AWS) IS LOCATED IN WHICH STATE/UT?\n(A)ANDAMAN AND NICOBAR ISLANDS\n(B)LAKSHADWEEP\n(C)KARNATAKA\n(D)PUDUCHERRY":"C","WHILE STUDYING THE CLEAN DEVELOPMENT MECHANISM WE READ ABOUT CEU WHICH IS A STANDARD UNIT COMPRISING 1 MILLION CUBIC TONNE CO2. WHAT IS THE CORRECT FULL FORM?\n(A)CERTIFIED EMISSION UNITS\n(B)CARBON EMISSION UNITS\n(C)CODIFIED EMISSION UNITS\n(D)NONE OF THE ABOVE":"A","THE GRIHA STANDARDS ARE RELATED TO?\n(A)ARCHITECTURE STANDARDS\n(B)DEFENSE STANDARDS\n(C)ENVIRONMENT STANDARDS\n(D)COST EFFECTIVENESS":"C","IN WHICH OF THE FOLLOWING AREAS, CLARK R BAVIN AWARDS ARE GIVEN?\n(A)SPORTS\n(B)WILDLIFE PROTECTION\n(C)FILMS & TELEVISION\n(D)JOURNALISM":"B","WHICH AMONG THE FOLLOWING IS THE “LEGALLY BINDING” CONVENTION?\n(A)UNITED NATIONS FRAMEWORK CONVENTION ON CLIMATE CHANGE\n(B)ASIA-PACIFIC PARTNERSHIP ON CLEAN DEVELOPMENT AND CLIMATE\n(C)VIENNA CONVENTION FOR THE PROTECTION OF THE OZONE LAYER\n(D)UNITED NATIONS CONVENTION TO COMBAT DESERTIFICATION":"D","WHICH AMONG THE FOLLOWING IS THE UNIT OF MEASUREMENT OF THE “ECOLOGICAL FOOTPRINT”?\n(A)GLOBAL HECTARE\n(B)GALLON PER CAPITA\n(C)CUBIC METER\n(D)MAN HOUR":"A","WHICH OF THE FOLLOWING IS THE LARGEST BRACKISH WATER LAGOON IN ASIA?\n(A)CHILIKA LAKE\n(B)LOKTAK LAKE\n(C)WULAR LAKE\n(D)NAL SAROVAR":"A","THE DALMA WILDLIFE SANCTUARY (DWS) IS LOCATED IN WHICH STATE?\n(A)MAHARASHTRA\n(B)BIHAR\n(C)JHARKHAND\n(D)WEST BENGAL":"C","THE DAROJI SLOTH BEAR SANCTUARY IS LOCATED IN WHICH STATE?\n(A)KARNATAKA\n(B)MAHARASHTRA\n(C)CHHATTISGARH\n(D)KERALA":"A","THE RATAPANI TIGER RESERVE (RTS) IS LOCATED IN WHICH STATE?\n(A)MADHYA PRADESH\n(B)SIKKIM\n(C)RAJASTHAN\n(D)KARNATAKA":"A","THE JAMBUGHODA WILDLIFE SANCTUARY (JWS) IS LOCATED IN WHICH STATE/UT?\n(A)NAGALAND\n(B)HARYANA\n(C)GUJARAT\n(D)TELANGANA":"C","POINTS CALIMERE BIRD SANCTUARY IS LOCATED IN WHICH OF THE FOLLOWING STATES?\n(A)KERALA\n(B)KARNATAKA\n(C)TAMIL NADU\n(D)WEST BENGAL":"C","REDD PLUS PROGRAMME IS CONCERNED WITH WHICH OF THE FOLLOWING?\n(A)NUCLEAR NON-PROLIFERATION TREATY (NPT)\n(B)CONVENTION ON BIOLOGICAL DIVERSITY (CBD)\n(C)MILLENNIUM DEVELOPMENT GOALS (MDG)\n(D)EARTH SUMMIT":"B","OZONE LAYER LIES IN:\n(A)TROPOSPHERE\n(B)TROPOPAUSE\n(C)STRATOSPHERE\n(D)PHOTOSPHERE":"C","RECENTLY, THE “BLUE BABY SYNDROME” OR “METHEMOGLOBINEMIA” HAS BEEN MAKING NEWS AS AN ENVIRONMENTALLY CAUSED CHILDREN’S HEALTH ISSUE. IN THIS DISEASE, THE INFANT’S BLOOD IS UNABLE TO CARRY ENOUGH OXYGEN TO BODY CELLS AND TISSUE. IT WAS PUBLISHED IN SOME RESEARCH PAPERS THAT THE GROUND WATER WITH LARGE CONCENTRATIONS OF ONE OF THE FOLLOWING SALTS CAUSES THE BLUE BABY SYNDROME. WHICH AMONG THE FOLLOWING IS THAT SALT?\n(A)PHOSPHATES\n(B)NITRATES\n(C)SULFATES\n(D)CARBONATES":"B","THE ESTABLISHMENT OF TAJ TRAPEZIUM ZONE (TTZ) ENSHRINES WHICH AMONG THE FOLLOWING OBJECTIVES?\n(A)PROTECTION FROM POLLUTION\n(B)TOURISM DEVELOPMENT\n(C)ECONOMY HUB\n(D)TRANSPORTATION FACILITIES":"A","WHICH AMONG THE FOLLOWING IS ONE OF THE LARGEST WINTERING GROUND FOR THE MIGRATORY WATERFALL IN INDIA?\n(A)GHANA SANCTUARY,RAJASTHAN\n(B)CHILKA LAKE,ORISSA\n(C)SULTANPUR BIRD SANCTUARY,HARYANA\n(D)DAL LAKE, KASHMIR":"B"}
            f()
        elif SUBJECT==4:
            SUB={"WHICH IS THE NATIONAL GAME OF INDIA-\n(A)CRICKET\n(B)FOOTBALL\n(C)HOCKEY\n(D)BASKET BALL":"C","NAME THE FIRST INTERNATIONAL CHESS PLAYER-\n(A)VISHWANATHAN ANAND\n(B)MANUEL AARON\n(C)S.VIJAYALAXMI\n(D)KONERU HUMPY":"B","IN WHICH YEAR DRONACHARYA AWARDS COMMENCED?\n(A)1990\n(B)1984\n(C)1976\n(D)1985":"D","WHO IS THE FIRST PLAYER TO BE HONOURED WITH BHARAT RATNA-\n(A)VISHWANATHAN ANAND\n(B)MARY KOM\n(C)SACHIN TENDULKAR\n(D)MILKHA SINGH":"C","IN WHICH YEAR ODI WORLD CUP STARTED?\n(A)1980\n(B)1975\n(C)1976\n(D)1979":"B","WHICH TEAM WON THE IPL TITLE IN 2016?\n(A)CSK\n(B)MI\n(C)RCB\n(D)SRH":"D","NAME THE FIRST INDIAN PLAYER TO GO HATRICK IN A TEST MATCH?\n(A)SHQANE WARNE\n(B)ANIL KUMBLE\n(C)HARBHAJAN SINGH\n(D)MUTTIAH MURALITHARAN":"C","WHERE IS BRABOURN CRICKET STADIUM SITUATED?\n(A)CHENNAI\n(B)CAPE TOWN\n(C)HIMACHAL PRADESH\n(D)MUMBAI":"D","NAME THE INDIAN WOMAN CRICKETER WHO MADE DOUBLE CENTURY IN A TEST MATCH?\n(A)HARMANPREET KAUR\n(B)MITHALI RAJ\n(C)VEDA KRISHNAMURTHY\n(D)THIRUSH KAMINI":"B","NAME THE CRICKETER WHO WAS THE QUICKEST TO CROSS 8000 MARK IN ONE DAY INTERNATIONAL MATCHES?\n(A)SUNIL GAVASKAR\n(B)SAURAV GANGULY\n(C)SACHIN TENDULKAR\n(D)VIRAT KHOLI":"D","WHAT IS THE NUMBER OF OLYMPIC GAMES TO BE HELD IN 2021?\n(A)21\n(B)29\n(C)33\n(D)40":"C","WHICH IS THE GOVERNING BODY OF FOOTBALL FEDERATIONS FROM AROUND THE WORLD?\n(A)FIFA: FEDERATIONS OF INTERNATIONAL FOOTBALL FEDERATIONS\n(B) IFA: INTERNATIONAL FOOTBALL FEDERATIONS\n(C)UIFA: UNION INTERNATIONAL FOOTBALL FEDERATIONS\n(D)FIFF: FEDERATION OF INTERNATIONAL FOOTBALL FEDERATIONS":"A","WHICH PLAYER HOLDS THE RECORD FOR MOST GOALS IN THE WORLD CUP FINALS?\n(A)MOROSLAV KLOSE\n(B)RONALDO FIRIMINO\n(C)LIONEL MESSI\n(D)CRISTIANO RONALDO":"A","WHEN WERE THE FIRST COMMON WEALTH GAMES HELD?\n(A)1930\n(B)1953\n(C)1949\n(D)1921":"A","THE FIRST OFFICIAL CRICKET MATCH WAS PLAYED BETWEEN-\n(A)ENGLAND AND WEST INDIES\n(B)ENGLAND AND AUSTRALIA\n(C)AUSTRALIA AND WEST INDIES\n(D)NONE OF THE ABOVE":"B","IN THE WORLD CUP OF ONE DAY,WHICH COUNTRY LOST MAXIMUM NUMBER OF FINALS?\n(A)PAKISTAN\n(B)ENGLAND\n(C)SOUTH AFRICA\n(D)WEST INDIES":"B","WHO IS THE CURRENT PRESIDENT OF FIFA?\n(A)JOSEPH BLATTER\n(B)GIANNI INFANTINO\n(C)PRINCE ALI BIN HUSSEIN\n(D)NONE OF THESE":"B","WHICH COUNTRY HAS WON THE MAXIMUM NUMBER OF HOCKEY WORLD CUPS?\n(A)AUSTRALIA\n(B)GERMANY\n(C)PAKISTAN\n(D)HOLLAND":"C","THE CRICKET WORLD CUP OF 2023 WILL BE HELD IN -\n(A)INDIA\n(B)ENGLAND\n(C)WEST INDIES\n(D)SOUTH AFRICA":"A","WHEN WAS THE FIRST OFFICIAL CRICKET MATCH WAS PLAYED-\n(A)1877\n(B)1870\n(C)1897\n(D)1896":"A"}
            f()
        elif SUBJECT==5:
            SUB={"THE BATTLE OF PLASSEY WAS FOUGHT IN-\n(A)1757\n(B)1782\n(C)1748\n(D)1764":"A","THE TERRITORY OF PORUS WHO OFFERED STRONG RESISTANCE TO ALEXANDER WAS SITUATED BETWEEN THE RIVERS OF-\n(A)SUTLEJ AND BEAS\n(B)JHELUM AND CHENAB\n(C)RAVI AND CHENAB\n(D)GANGA AND YAMUNA":"B","UNDER AKBAR,THE MIR BAKSHI WAS REQUIRED TO LOOK AFTER-\n(A)MILITARY AFFAIRS\n(B)THE STATE TREASURY\n(C)THE ROYAL HOUSEHOLD\n(D)THE LAND REVENUE SYSTEM":"A","TRIPITAKAS ARE THE SACRED BOOKS OF-\n(A)BUDDHISTS\n(B)HINDUS\n(C)JAINS\n(D)NONE OF THE ABOVE":"A","THE TRIDENT-SHAPED SYMBOL OF BUDDHISM DOES NOT REPRESENT-\n(A)NIRVANA\n(B) SANGHA\n(C)BUDDHA\n(D)DHAMMA":"A","THE THEORY OF ECONOMIC DRAIN OF INDIA DURING BRITISH IMPERIALISM WAS PROPOUNDED BY-\n(A)JAWAHARLAL NEHRU\n(B)DADABHAI NAROJI\n(C)R.C.DUTT\n(D)M.K.GANDHI":"B","THE TREATY OF SRIRANGAPATNA WAS SIGNED BETWEEN TIPU SULTAN AND-\n(A)ROBERT CLIVE\n(B)CORNWALLIS\n(C)DALHOUSIE\n(D)WARREN HASTINGS":"B","THE SYSTEM OF COMPETITIVE EXAMINATION FOR CIVIL SERVICE WAS ACCEPTED IN PRINCIPLE IN THE YEAR-\n(A)1833\n(B)1854\n(C)1858\n(D)1882":"B","THROUGH WHICH ONE OF THE FOLLOWING, THE KING EXERCISED HIS CONTROL OVER VILLAGES IN THE VIJAYANAGAR EMPIRE?\n(A)DANNAYAKA\n(B)SUMANTA\n(C)NAYAKA\n(D)MAHANAYAKACHARYA":"D","THE VIJAYANAGARA RULER, KRISHNADEV RAYA'S WORK AMUKTAMALYADA WAS IN-\n(A)TELUGU\n(B)SANSKRIT\n(C)TAMIL\n(D)KANNADA":"A","UNDER AN AGREEMENT WITH WHICH OF THE FOLLOWING COUNTRIES DID SUBHAS CHANDRA BOSE ORGANIZE THE INDIAN SOLDIERS, TAKEN AS PRISONERS BY THE AXIS POWERS, INTO THE AZAD HIND FAUJ?\n(A)CHINA\n(B)GERMANY\n(C)ITALY\n(D)JAPAN":"D","WE HEAR OF TWO ENVOYS BEING SENT TO THE ROMAN KINGS, ONE IN 27-28 AD TO THE COURT OF AUGUSTUS AND THE OTHER IN 110-20 AD TO THE COURT OF-\n(A)CARTIUS\n(B)TRAJAN\n(C)NERO\n(D)BRUTUS":"B","THE USE OF KHAROSHTI IN ANCIENT INDIAN ARCHITECTURE IS THE RESULT OF INDIA'S CONTACT WITH-\n(A)CENTRAL ASIA\n(B)IRAN\n(C)GREECE\n(D)CHINA":"C","VAIKHANASA THE FIVE-FOLD CONCEPTION OF VISHNU CONSISTS OF-\n(I)BRAHMAN\n(II)PURUSHA\n(III)PRAKIRTI\n(IV)SATYA\n(V)ACHYUTA\n(VI)ANIRUDDHA\n\n(A)I,II,III,IV AND V\n(B)II,III,IV,V AND VI\n(C)I,II,IV,V AND VI\n(D)I,III,IV,V AND VI":"D","THE TROOPS RAISED BY THE EMPEROR BUT NOT PAID DIRECTLY THE STATE AND PLACE UNDER THE CHARGE OF MANSABADARS WERE KNOWN AS-\n(A)WALASHAHI\n(B)BARAWARDI\n(C)JCUMAKI\n(D)DAKHILI":"D","THE TREATY OF MANGAlORE WAS SIGNED BETWEEN-\n(A)THE ENGLISH EAST INDIA COMPANY AND HAIDAR ALI\n(B)THE ENGLISH EAST INDIA COMPANY AND TIPU SULTAN\n(C)HAIDAR ALI AND THE ZAMORIN OF CALICUT\n(D)THE FRENCH EAST INDIA COMPANY AND TIPU SULTAN":"B","TO CONQUER AND ANNEX PESHAWAR AND PUNJAB, MAHMUD OF GHAZNI DEFEATED-\n(A)GHURIDS\n(B)ARABS\n(C)KARKOTAKAS\n(D)HINDUSHAHIS":"D","TO WHICH PROFESSIONS EARLIER LEADERS WHO STRUGGLED FOR FREEDOM OF INDIA MAINLY BELONGED?\n(A)LAWYERS\n(B)TEACHERS\n(C)JOURNALISTS\n(D)ALL OF THE ABOVE":"D","THE VICTORIES OF KARIKALA ARE WELL PORTRAYED IN-\n(A)PALAMOLI\n(B)ARUVANAD\n(C)PATTINAPPALAI\n(D)PADIRRUPATTU":"C","TODAR MAL WAS ASSOCIATED WITH-\n(A)MUSIC\n(B)LITERATURE\n(C)FINANCE\n(D)LAW":"C"}
            f()
        else:
            print("INVALID VALUE TAKEN.")
            print()
            while SUBJECT!=1 and SUBJECT!=2 and SUBJECT!=3 and SUBJECT!=4 and SUBJECT!=5:
                print("TRY AGAIN!")
                SUBJECT=1
            continue
        print()
        print("YOUR SCORE IS:")
        if NUM>9:
            if C<10:
                print("--------")
                print("| ",C,"  |")
                print("--------")
                print("| ",NUM," |")
                print("--------")
            if C>9:
                print("--------")
                print("| ",C," |")
                print("--------")
                print("| ",NUM," |")
                print("--------")
        if NUM<10:
            print("-------")
            print("| ",C," |")
            print("-------")
            print("| ",NUM," |")
            print("-------")
        
        print()
        ans=input("DO YOU WANT TO CONTINUE? ('ENTER' FOR YES OR 'ANY OTHER KEY FOLLOWED BY ENTER' FOR NO): ")
        if ans=="":
            print()
            count+=1
            MG=int(input("WHICH TYPE OF GAME DO YOU WANT TO PLAY?\n\n1. FUN GAMES\n2. MIND GAME\n3. IQ GAME)\n\nENTER YOUR CHOICE: "))
        else:
            break

    elif MG==3:
            print()
            print("FPB IS A NUMBER PUZZLE GAME. YOUR TASK IS SIMPLY TO GUESS A NUMBER FOR WHICH CERTAIN HINTS WILL BE PROVIDED TO YOU.")
            print()
            print("HOW TO PLAY THE GAME:")
            print()
            print("PICO MEANS 'ONE DIGIT IS CORRECT BUT IN THE WRONG POSITION.'")
            print("FERMI MEANS 'ONE DIGIT IS CORRECT AND IN THE RIGHT POSITION.'")
            print("BAGELS MEANS 'NO DIGIT IS CORRECT.'")
            print("THERE ARE NO REPEATED DIGITS IN THE NUMBER.")
            print()
            print("WHICH TYPE OF FPB YOU WANT TO PLAY?")
            print()
            print("1. SINGLE PLAYER")
            print("2. MULTI PLAYER")
            print()
            FPB=int(input("ENTER 1 FOR SINGLE PLAYER AND 2 FOR MULTI PLAYER: "))
            while FPB!=1 and FPB!=2:
                print()
                print("INVALID CHOICE")
                FPB=int(input("ENTER 1 FOR SINGLE PLAYER AND 2 FOR MULTI PLAYER: "))
            print()
            if FPB==1:
                d=3
                n=str(randint(100,999))
                while n[0]==n[1] or n[1]==n[2] or n[2]==n[0]:
                    n=str(randint(100,999))
                print("I HAVE THOUGHT UP A NUMBER. YOU HAVE 10 GUESSES TO GET IT.")
                c=1
                while True:
                    print("GUESS #",c)
                    g=input()
                    if len(g)!=d:
                        print("WRONG NUMBER OF DIGITS. TRY AGAIN.")
                        continue
                    hint=[]
                    for i in range(d):
                        if g[i]==n[i]:
                            hint.append("FERMI")
                        elif g[i] in n:
                            hint.append("PICO")
                    shuffle(hint)
                    if len(hint)==0:
                        print("BAGELS")
                    else:
                        print(" ".join(hint))
                    c+=1
                    if g==n:
                        print("VOILA! YOU GOT THE RIGHT NUMBER.")
                        break
                    if c>10:
                        print("YOU RAN OUT OF MOVES.")
                        print("THE NUMBER GUESSED BY ME WAS",n)
                        print("BETTER LUCK NEXT TIME.")
                        break
            elif FPB==2:
                d=3
                n=str(randint(100,999))
                while n[0]==n[1] or n[1]==n[2] or n[2]==n[0]:
                    n=str(randint(100,999))
                print("IF ANY OF THE PLAYERS WANT TO SURRENDER, JUST PRESS ENTER.")
                print()
                c1=1
                PLAYER1=input("ENTER THE NAME OF THE 1ST PLAYER: ")
                PLAYER2=input("ENTER THE NAME OF THE 2ND PLAYER: ")
                print()
                g=" "
                while g!="":
                    print(PLAYER1,"YOUR TURN NOW.")
                    print()
                    while True:
                        print("GUESS #",c1)
                        g=input()
                        if g!="":
                            if len(g)!=d:
                                print("WRONG NUMBER OF DIGITS. TRY AGAIN.")
                                continue
                            hint=[]
                            for i in range(d):
                                if g[i]==n[i]:
                                    hint.append("FERMI")
                                elif g[i] in n:
                                    hint.append("PICO")
                            shuffle(hint)
                            if len(hint)==0:
                                print("BAGELS")
                            else:
                                print(" ".join(hint))
                            c1+=1
                            if g==n:
                                print("VOILA! YOU GOT THE RIGHT NUMBER.")
                                break
                            if c1>100:
                                print("YOU RAN OUT OF MOVES.")
                                print("THE NUMBER GUESSED BY ME WAS",n)
                                print("BETTER LUCK NEXT TIME.")
                                break
                        elif g=="":
                            print("YOU SURRENDERED.")
                            print("SO YOU LOST.")
                            print("THE NUMBER WAS ",n)
                            print(PLAYER2,"WON THE MATCH.")
                            break
                    if g=="":
                        break
                    print()
                    print(PLAYER2,"YOUR TURN NOW.")
                    print()
                    n=str(randint(100,999))
                    while n[0]==n[1] or n[1]==n[2] or n[2]==n[0]:
                        n=str(randint(100,999))
                    c2=1
                    while True:
                        print("GUESS #",c2)
                        g=input()
                        if g!="":
                            if len(g)!=d:
                                print("WRONG NUMBER OF DIGITS. TRY AGAIN.")
                                continue
                            hint=[]
                            for i in range(d):
                                if g[i]==n[i]:
                                    hint.append("FERMI")
                                elif g[i] in n:
                                    hint.append("PICO")
                            shuffle(hint)
                            if len(hint)==0:
                                print("BAGELS")
                            else:
                                print(" ".join(hint))
                            c2+=1
                            if g==n:
                                print("VOILA! YOU GOT THE RIGHT NUMBER.")
                                break
                            if c1>100:
                                print("YOU RAN OUT OF MOVES.")
                                print("THE NUMBER GUESSED BY ME WAS",n)
                                print("BETTER LUCK NEXT TIME.")
                                break
                        elif g=="":
                            print("YOU SURRENDERED.")
                            print("SO YOU LOST.")
                            print("THE NUMBER WAS ",n)
                            print(PLAYER1,"WON THE MATCH.")
                            break
                    if g=="":
                        break
                    g=""
                    c1=c1-1
                    c2=c2-1
                    print()
                    print(PLAYER1,"HAS USED",c1,"TRIES TO GUESS THE NUMBER.")
                    print()
                    print(PLAYER2,"HAS USED",c2,"TRIES TO GUESS THE NUMBER.")
                    print()
                    if c1>c2:
                        print()
                        print(PLAYER2,"HAS WON THE MATCH AND",PLAYER1,"HAS LOST THE MATCH.")
                        print()
                    if c1==c2:
                        print()
                        print(PLAYER1,"AND",PLAYER2,"HAS TAKEN EQUAL TRIES TO GUESS THE NUMBER.")
                        print()
                    if c1<c2:
                        print()
                        print(PLAYER1,"HAS WON THE MATCH AND",PLAYER2,"HAS LOST THE MATCH.")
                        print()

            print()
            ans=input("DO YOU WANT TO CONTINUE? ('ENTER' FOR YES OR 'ANY OTHER KEY FOLLOWED BY ENTER' FOR NO): ")
            if ans=="":
                print()
                count+=1
                MG=int(input("WHICH TYPE OF GAME DO YOU WANT TO PLAY?\n\n1. FUN GAMES\n2. MIND GAME\n3. IQ GAME)\n\nENTER YOUR CHOICE: "))
            else:
                break

    if MG>3:
        MG=int(input("ENTER A VALID CHOICE (1/2/3): "))
        print()

