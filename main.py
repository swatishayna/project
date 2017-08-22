#importing spy_details.py file
from spy_details import spy
from start_chat import start_chat

print "LET US GET STARTED "
question = "Continue as " + spy["salutation"] + "." + spy["name"] + "(Y/N)?"
#question = "Continue as " + spy["salutation"] + "." + spy["name"] + "(Y/N)?"
existing = raw_input(question)

#validating user's input
#TO CHECK WHETHER THE USER WANTS TO CONTINUE AS DEFAULT USER OR NOT
if existing == "Y" or existing == "y" :
    spy_name = spy["salutation"] + " " + spy["name"]
    start_chat(spy["name"] , spy["age"] , spy["rating"] ,spy["is_online"] )
elif (existing == "N" or existing == "n") :
    spy["name"] = raw_input("Provide your name here :")  # raw_input(): function that returns string only
    if len(spy["name"]) > 0:  # to check whether spy has input some name or not
        if not spy["name"].isalpha():
            print  "INVALID SPY_NAME INPUT "
            spy["name"] = raw_input("ENTER YOUR NAME HERE AGAIN: ")
        else:
            print "VALID SPY_NAME INPUT"
            spy["salutation"] = raw_input("What should we call you Mr. or Ms?")
            spy["name"]= spy["salutation"] + " " + spy["name"]
            while True:
                try:
                    spy["age"] = int(raw_input("Enter your age here: "))  # int() : used for typecasting string into int

                except ValueError:
                    print "enter valid age. Try again."
                if spy["age"] > 12 and spy["age"] < 50:
                    print "You are good to go."
                    spy["rating"] = float(raw_input("Enter your rating here: "))
                    if spy["rating"] > 4.5:
                        print "good"
                    elif spy["rating"] > 3.5 and spy["rating"] <= 4.5:
                        print "excellent"
                    elif spy["rating"] >= 2.5 and spy["rating"] <= 3.5:
                        print "you can do better"
                    else:
                        print "need improvement"
                    spy["is_online"  ] = True

                #starting chat application
                    start_chat(spy["name"], spy["age"] , spy["rating"], spy["is_online"])
                else:
                    print "You do not satisfy the required age condition. "
    else:
        print "A spy needs to have valid name.Try again."
else:
    print "WRONG CHOICE"



