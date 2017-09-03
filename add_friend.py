# import statements
from globals import friends
import re
# importing spy_details.py file
from spy_details import spy


# add new friend


def add_friend():
    new_friend = \
        {
            "name": " ",
            "salutation": " ",
            "age": 0,
            "rating": 0.0,
            "is_online": False,
            "chats": []
        }
    new_friend["name"] = raw_input("Please add your friend's name: ")
    if len(spy["name"]) > 0:
        # regular expression which matches only alphabets
        pattern5 = '^[a-zA-Z\s]+$'
        if re.match(pattern5, new_friend["name"]) is not None:
            # string matched
            new_friend["salutation"] = raw_input("Are they Mr or Ms ? ")
            pattern6 = '^[M][r s]$'
            if re.match(pattern6, new_friend["salutation"]) is not None:
                print "Checking .."
                new_friend["name"] = new_friend["salutation"] + " " + new_friend["name"]
                new_friend["age"] = raw_input("Age? ")
                pattern7 = '^[0-9]+$'
                if re.match(pattern7, new_friend["age"]) is not None:
                    print "CHECKING..."
                    new_friend["rating"] = raw_input("Spy Rating")
                    if len(new_friend["name"]) > 0:
                        if new_friend["age"] > 12 < 50:
                            # add friend
                            friends.append(new_friend)
                            return len(friends)
                        else:
                            print " Sorry! Invalid entry. We cant add spy with the details you provided"
                    else:
                        print " Sorry! Invalid entry. We cant add spy with the details you provided"
                else:
                    print "Input friend's age format is not valid"
            else:
                print "Input friend salutation's format is not valid. "
        else:
            print "Input friend name's format  is not valid"
    else:
        print "Enter valid name to continue "
