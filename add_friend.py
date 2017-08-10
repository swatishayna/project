def add_friend():
    friends_name = []
    friends_age = []
    friends_rating = []
    friends_is_online = []

    new_name = raw_input(" Please add your friend's name: ")
    new_salutation = raw_input("Are they Mr or Ms ? ")
    new_name =  new_name + " " + new_salutation
    new_age = raw_input("Age? ")
    new_rating = raw_input(" Spy Rating")

    new_age = int(new_age)
    new_rating = float(new_rating)
    if len(new_name) > 0 :
       #ADDFRIEND
       friends_name.append(new_name)
       friends_age.append(new_rating)
       friends_rating.append(new_rating)
       friends_status.append(True)

    else:
        print " Sorry! Invalid entry. We cant add spy with the details you provided"
    return (friends_name)