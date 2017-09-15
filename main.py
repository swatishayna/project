# importing spy_details.py file
from spy_details import spy
# importing start_chat.py file
from start_chat import start_chat
import re


print "LET US GET STARTED "

question = "Continue as " + spy["salutation"] + "." + spy["name"] + "(Y/N)?"
existing = raw_input(question)

# to check whether the user wants to continue as default user or not
if existing == "Y" or existing == "y":
    spy["name"] = spy["salutation"] + " " + spy["name"]
    start_chat(spy["name"], spy["age"], spy["rating"], spy["is_online"])
elif existing == "N" or existing == "n":
    spy["name"] = raw_input("Provide your name here :")  # raw_input(): function that returns string only
    # validating user's input
    # to check whether spy has input some name or not
    if len(spy["name"]) > 0:
        # regular expression which matches only alphabets
        pattern1 = '^[a-zA-Z\s]+$'
        if re.match(pattern1, spy["name"]) is not None:
            # string matched
            spy["salutation"] = raw_input("What should we call you Mr or Ms?")
            pattern2 = '^[M][r s]$'
            if re.match(pattern2, spy["salutation"]) is not None:
                spy["name"] = spy["salutation"] + " " + spy["name"]
                spy["age"] = raw_input("Provide your age here: ")
                pattern3 = '^[0-9]+$'
                if re.match(pattern3, spy["age"]) is not None:
                    print "CHECKING..."
                    if spy["age"] > 12 < 50:  # greater than 12 and less than 50
                        print "You are good to go."
                        spy["rating"] = raw_input("Enter your rating here: ")
                        pattern4 = '^[0-9]+\.[0-9]+$'
                        if re.match(pattern4, spy["rating"]) is not None:
                            print "CHECKING.."
                            if spy["rating"] > 4.5:
                                print "good"
                            elif spy["rating"] > 3.5 <= 4.5:
                                print "excellent"
                            elif spy["rating"] >= 2.5 <= 3.5:
                                print "you can do better"
                            else:
                                print "need improvement"
                            spy["is_online"] = True
                            # starting chat application
                            start_chat(spy["name"], spy["age"], spy["rating"], spy["is_online"])
                        else:
                            print"Input rating format is invalid"
                    else:
                        print "You do not satisfy the required age condition. "
                else:
                    print "Input age format is invalid"
            else:
                print "Enter suitable salutation "
        else:
            print "Input name format is invalid"
    else:
        print "A spy needs to have valid name.Try again."
else:
    print "Wrong Choice"
