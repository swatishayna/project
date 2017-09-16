# importing start_chat.py file
from start_chat import start_chat
import re
from colorama import Fore,init
from spy_info_class import Spy_Info
init()
si = Spy_Info()
print "LET US GET STARTED "

question = "Continue as " + si.get_salutation() + "." + si.get_name() + "(Y/N)?"
existing = raw_input(question)

# to check whether the user wants to continue as default user or not
if existing == "Y" or existing == "y":
    print Fore.GREEN + "Authentication complete." + Fore.RESET + "\nWelcome " + si.get_name() + "\n" + "age: ", si.get_age(), "\nRating: ", si.get_rating(), "\nOnline: ", si.get_online();

    start_chat(si)
elif existing == "N" or existing == "n":
    spy_name = raw_input("Provide your name here :")  # raw_input(): function that returns string only
    # validating user's input
    # to check whether spy has input some name or not
    if len(spy_name) > 0:
        # regular expression which matches only alphabets
        pattern1 = '^[a-zA-Z\s]+$'
        if re.match(pattern1, spy_name) is not None:
            # string matched
            salutation = raw_input("What should we call you Mr or Ms?")
            pattern2 = '^[M][r s]$'
            if re.match(pattern2, salutation) is not None:
                spy_name = salutation + " " + spy_name
                spy_age = raw_input("Provide your age here: ")
                pattern3 = '^[0-9]+$'
                if re.match(pattern3, spy_age) is not None:
                    print "CHECKING..."
                    if spy_age > 12 < 50:  # greater than 12 and less than 50
                        print "You are good to go."
                        spy_rating = raw_input("Enter your rating here: ")
                        pattern4 = '^[0-9]+\.[0-9]+$'
                        if re.match(pattern4, spy_rating) is not None:
                            print "CHECKING.."
                            if spy_rating > 4.5:
                                print "good"
                            elif spy_rating > 3.5 <= 4.5:
                                print "excellent"
                            elif spy_rating >= 2.5 <= 3.5:
                                print "you can do better"
                            else:
                                print "need improvement"
                            spy_is_online = True
                            # starting chat application
                            start_chat(spy_name,salutation, spy_age, spy_rating, spy_is_online)
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
