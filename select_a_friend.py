from globals import friends


def select_a_friend():
    # to increase the counter for printing friend from friends, used as flag
    counter = 1
    for friend in friends :
        print str(counter) + ". " + friend["name"] + "Age : " + str(friend["age"])
        counter = counter + 1
    result = int(raw_input("Select from the list : "))
    return result-1

