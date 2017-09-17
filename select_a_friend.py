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
            result = int(raw_input("Select from the list : "))

            f = open( str(result))
            lines = f.read()
            match = re.findall('^[0-9]+$' , lines)
            print match
            result = int(result)
            if result > 0 and result < counter:
                return result-1
            else:
                return "collapsed"

