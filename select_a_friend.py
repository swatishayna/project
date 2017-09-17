from globals import friends
from colorama import init, Fore
import re,sys


init()


def select_a_friend():
    # to increase the counter for printing friend from friends, used as flag
    counter = 1
    for friend in friends:
        print str(counter) + ". " + friend["name"] + "Age : " + str(friend["age"])
        counter = counter + 1

    while True:
        result = raw_input("Select from the list : ")

        pattern19 = '^[0-9]+$'
        if re.match(pattern19, result) is not None:
            result = int(result)
            if result > 0 and result < counter:
                return result - 1
            else:
                return None
            break
        else:
            print " input integer value"

