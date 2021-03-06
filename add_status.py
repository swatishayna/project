# import statements
from globals import STATUS_MESSAGES
from colorama import init, Fore

# updated status message
updated_status_message = None


def add_status(current_status_message):
    global updated_status_message
    if current_status_message is not None:
        print "Your current status is  " + current_status_message + "\n"
    else:
        print " provide some status"

    # ask user for choosing from older messages.
    default = raw_input("Do you want to select from the older status (y/n?)")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        # validating user's input
        if len(new_status_message) > 0:
            # adding new status to the list
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
            print "Your updated status message is %s" % updated_status_message
        else:
            print  Fore.RED + "You did not provide any status message"
    elif default.upper() == "Y":
        # counter for serial number of messages
        item_position = 1

        # printing all older messages
        for message in STATUS_MESSAGES:
            print str(item_position) + " . " + message
            item_position = item_position + 1
            # asking user's choice.
        message_selection = int(raw_input("\nChoose from the above messages  "))

        # validating user's input
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
            print "Your updated message is: " + updated_status_message
        else:
            print  Fore.RED + "Invalid choice. Try again. "
    else:
        print  Fore.RED + "The option you chose is Invalid. "
    return updated_status_message
