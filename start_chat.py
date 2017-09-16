from add_status import add_status,STATUS_MESSAGES
from add_friend import add_friend
from send_message import send_message
from read_message import read_message
from globals import friends
import time
import read_chat_history
from colorama import Fore, init
import spy_details
import spy_info

init()


# start_chat() definition
def start_chat( name, age, rating, status):
    from globals import current_status_message
    error_message = None  # variable for storing error message
    if not (age > 12 < 50):  # validating user's details
        error_message = " INVALID AGE. PROVIDE VALID AGE!"
        print error_message
    else:

        welcome_message = Fore.BLUE + "AUTHENTICATION COMPLETED. WELCOME\n  " + \
                          Fore.BLUE + "Name : " + name + "\n  " + \
                          Fore.BLUE + "Age : " + str(age) + "\n  " + \
                          Fore.BLUE + "Rating: " + str(rating) + "\n  " + \
                          Fore.BLUE + "Proud to have you here"
        print welcome_message

        # displaying menu for user
        show_menu = True
        while show_menu:
            time.sleep(1)
            menu_choices = Fore.LIGHTMAGENTA_EX + "What do you want to do ?\n" + Fore.RESET + \
                           Fore.LIGHTMAGENTA_EX + " 1.ADD A STATUS UPDATE \n" + Fore.RESET + \
                           Fore.LIGHTMAGENTA_EX + " 2.ADD A FRIEND \n" + Fore.RESET + \
                           Fore.LIGHTMAGENTA_EX + " 3.SEND A SECRET MESSAGE \n" + Fore.RESET + \
                           Fore.LIGHTMAGENTA_EX + " 4.READ A SECRET MESSAGE \n" + Fore.RESET + \
                           Fore.LIGHTMAGENTA_EX + " 5.READ CHATS FROM A USER \n" + Fore.RESET + \
                           Fore.LIGHTMAGENTA_EX + " 6.CLOSE APPLICATION \n  "
            result = int(raw_input(menu_choices))

            # validating user's input
            if result == 1:
                time.sleep(1)
                current_status_message = add_status(current_status_message)
                time.sleep(1)
                print 'your status has been updated to :\n', current_status_message

            elif result == 2:
                time.sleep(1)
                number_of_friends = add_friend()
                print 'You have %d friends' % number_of_friends
                show_friends();

            elif result == 3:
                time.sleep(1)
                send_message()
            elif result == 4:
                time.sleep(1)
                read_message();
            elif result == 5:
                time.sleep(1)
                read_chat_history();
            elif result == 6:
                show_menu = False
                time.sleep(1)
                print Fore.RED + "Application is closed now."
            else:
                print "WRONG CHOICE"  # exit from application


def show_friends():
    position = 1
    for i in friends:
        print position, ". " + i.get_name()
        position = position + 1