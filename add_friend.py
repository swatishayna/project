# import statements
from globals import friends
import re
import spy_info_class
from colorama import Fore,init
from spy_info_class import Spy_Info

def add_friend():
    friend_obj = Spy_Info("Mr.", "Guest", 24, 3.6, True)

    friend_obj.name = raw_input("Please add your friend's name: ")
    if len(friend_obj.name) > 0:
        # regular expression which matches only alphabets
        pattern5 = '^[a-zA-Z\s]+$'
        if re.match(pattern5, friend_obj.name) is not None:
            # string matched
            friend_obj.salutation = raw_input("Are they Mr or Ms ? ")
            pattern6 = '^[Mm][r s]$'
            if re.match(pattern6, friend_obj.salutation) is not None:
                print "CHECKING .."
                friend_obj.name =friend_obj.salutation + " " + friend_obj.name
                friend_obj.age = raw_input("Age? ")
                pattern7 = '^[0-9]+$'
                if re.match(pattern7, friend_obj.age) is not None:
                    print "CHECKING..."

                    friend_obj.rating = raw_input("Spy Rating")
                    pattern7 = '^[0-9]+\.[0-9]+$'
                    if re.match(pattern7, friend_obj.rating) is not None:
                        print "CHECKING.."
                        if len(friend_obj.name) > 0 and friend_obj.age > 12 < 50:
                            # add friend
                            friends.append(friend_obj)
                            return len(friends)

                        else:
                            print Fore.RED + " Sorry! Invalid entry. We cant add spy with the details you provided"
                    else:
                        print Fore.RED + " Input friend rating format is invalid"
                else:
                    print Fore.RED + "Input friend's age format is invalid"
            else:
                print Fore.RED + "Input friend salutation's format is invalid. "
        else:
            print Fore.RED + "Input friend name's format  is invalid"
    else:
        print Fore.RED + "Enter valid name to continue"