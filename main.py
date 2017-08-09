#importing spy_details.py file
from spy_details import spy_name , spy_salutation ,spy_age , spy_rating
#importing start_chat.py
import start_chat
print "Let us get started!"
question = "Continue as " + spy_salutation + "." + spy_name + "(Y/N)?"
existing = raw_input(question)

#validating user's input
if existing == "Y" or existing == "y" :
    start_chat.start_chat(spy_name , spy_age , spy_rating )
elif (existing == "N" or existing == "n") :
    spy_name = raw_input("Provide your name here :")  # raw_input(): function that returns string only
    if len(spy_name) > 0:  # to check whether spy has input some name or not
        if not spy_name.isalpha():
            print  "INVALID SPY_NAME INPUT "
            spy_name = raw_input("ENTER YOUR NAME HERE AGAIN: ")
        else:
            print "VALID SPY_NAME INPUT"
            spy_age = 0
            spy_rating = 0.0
            spy_is_online = False

            spy_salutation = raw_input("What should we call you Mr. or Ms?")
            spy_age = int(raw_input("Enter your age here: "))  # int() : used for typecasting string into int
            if spy_age > 12 and spy_age < 60:
                print "You are good to go."
                spy_rating = float(raw_input("Enter your rating here: "))
                if spy_rating > 4.5:
                    print "good"
                elif spy_rating > 3.5 and spy_rating <= 4.5:
                    print "excellent"
                elif spy_rating >= 2.5 and spy_rating <= 3.5:
                    print "you can do better"
                else:
                    print "need improvement"
                spy_is_online = True
                print "Authentication Completed. Welcome " + spy_name + "age: " + str(
                    spy_age) + " and rating of: " + str(spy_rating) + " proud to have you."

            else:
                print "You are not a valid user."

            spy_name = spy_salutation + " " + spy_name  # CONCATENATION OF SALUTATION AND NAME.
            print 'Welcome ' + spy_name + '. Glad to have you back with us.'
            print "Alright " + spy_name + " I would like to know more about you."
    else:
        print "A spy needs to have valid name.Try again."



else:
    print " WrONG CHOICE"

