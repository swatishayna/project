#import statements
from globals import friends

#ADD NEW FRIENDS
def add_friend():
    new_friend = {
         "name": " ",
         "salutation": " " ,
         "age": 0 ,
         "rating":0.0 ,
         "is_online": False
    }
    new_friend["name"] = raw_input(" Please add your friend's name: ")
    new_friend["salutation"] = raw_input("Are they Mr or Ms ? ")
    new_friend["name"] =  new_friend["salutation"] + " " + new_friend["name"]

    new_friend["age"] = int(raw_input("Age? "))
    new_friend["rating"] = float(raw_input(" Spy Rating"))


    if len( new_friend["name"]) > 0 and  new_friend["age"] > 12 and  new_friend["age"] < 50 :
       #ADDFRIEND
       friends.append( new_friend)
       print "Friend is Added!"

    else:
        print " Sorry! Invalid entry. We cant add spy with the details you provided"
    return len(friends)