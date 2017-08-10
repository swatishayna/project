def add_status(current_status_message):

    if current_status_message != None:
        print "Your current status is  " + current_status_message + "\n"
    else:
        print " provide some status"
    default = raw_input("Do you want to select from the older status (y/n?)")
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")
        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
        elif default.upper() == "Y" :
            item_position = 1
            for message in STATUS_MESSAGES:
                print item_position + " . " + message
                item_position = item_position + 1
            message_selection = int(raw_input("\n Choose from the above messages  "))
            if len(STATUS_MESSAGES) >= message_selection:
                updated_status_message = STATUS_MESSAGES[message_selection -1]
                return updated_status_message