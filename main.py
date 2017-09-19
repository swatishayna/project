# importing start_chat.py file
from start_chat import start_chat
import re
from colorama import Fore, init
from spy_info_class import Spy_Info

init()

si = Spy_Info("Mr.", "Bond", 25, 4.6, True)

print "LET US GET STARTED "

question = "Continue as " + si.get_salutation() + "." + si.get_name() + "(Y/N)?"
existing = raw_input(question)

# to check whether the user wants to continue as default user or not
if existing == "Y" or existing == "y":
    start_chat(si)
elif existing == "N" or existing == "n":
    si.name = raw_input("Provide your name here :")  # raw_input(): function that returns string only
    # validating user's input
    # to check whether spy has input some name or not
    if len(si.name) > 0:
        # regular expression which matches only alphabets
        pattern1 = '^[a-zA-Z\s]+$'
        if re.match(pattern1, si.name) is not None:
            # string matched
            si.salutation = raw_input("What should we call you Mr or Ms?")
            pattern2 = '^[M][r s]$'
            if re.match(pattern2, si.salutation) is not None:
                si.name = si.salutation + " " + si.name
                si.age = raw_input("Provide your age here: ")
                pattern3 = '^[0-9]+$'
                if re.match(pattern3, si.age) is not None:
                    print "CHECKING..."
                    if si.age > 12 < 50:  # greater than 12 and less than 50
                        print "You are good to go."
                        si.rating = raw_input("Enter your rating here: ")
                        pattern4 = '^[0-9]+\.[0-9]+$'
                        if re.match(pattern4, si.rating) is not None:
                            print "CHECKING.."
                            if si.rating > 4.5:
                                print "good"
                            elif si.rating > 3.5 <= 4.5:
                                print "excellent"
                            elif si.rating >= 2.5 <= 3.5:
                                print "you can do better"
                            else:
                                print "need improvement"
                            spy_is_online = True
                            # starting chat application
                            start_chat(si)
                        else:
                            print Fore.RED + "Input rating format is invalid"
                    else:
                        print Fore.RED + "You do not satisfy the required age condition. "
                else:
                    print Fore.RED + "Input age format is invalid"
            else:
                print Fore.RED + "Enter suitable salutation "
        else:
            print Fore.RED + "Input name format is invalid"
    else:
        print Fore.RED + "A spy needs to have valid name.Try again."
else:
    print Fore.RED + "Wrong Choice"
