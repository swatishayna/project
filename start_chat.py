#IMPORTING TWO FILES HERE
from add_status import add_status
from add_friend import add_friend
from send_message import send_message
from read_message import read_message

#start_cHat() definition
def start_chat(name , age , rating, status ):
    from  globals import current_status_message
    #validating user's details
    error_message = None       #variable for storing error message
    if not (age > 12 and age < 50):
        error_message = " INVALID AGE. PROVIDE VALID AGE"
        print error_message
    else:
        welcome_message = "AUTHENTICATION COMPLETED. Welcome\n  " \
                          "Name : " + name + "\n" \
                          "Age : " + str(age) + "\ n" \
                          "\Rating: " + str(rating) + "\n " \
                          "Proud to have you here"
        print welcome_message

        #displaying menu for user
        show_menu = True
        while show_menu :
            menu_choices = "What do you want to do ?\n" \
                       " 1.ADD A STATUS UPDATE \n" \
                       " 2.ADD A FRIEND \n" \
                       " 3.SEND A SECRET MESSAGE \n" \
                       " 4.READ A SECRET MESSAGE \n" \
                       " 5.READ CHATS FROM A USER \n" \
                       " 6.CLOSE APPLICATION \n"
            result = int(raw_input(menu_choices))

        #validating user's input
            if   (result == 1) :
                current_status_message = add_status(current_status_message)

            elif (result == 2) :
                number_of_friends = add_friend()
                print "You have %d friends" %(number_of_friends)
            elif(result == 3) :
                send_message()
            elif(result == 4) :
                read_message()
            elif(result == 6):
            #close application
                show_menu = False
            else:
             print "WRONG CHOICE"   #EXIT FROM APPLICATION

