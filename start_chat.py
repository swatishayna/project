#start_chat() definition
def start_chat(name , age , rating):
    show_menu = True
    while show_menu :
        menu_choices = "What do you want to do? \n 1.ADD STATUS \n 2.CLOSE APPLICATION"
        result = int(raw_input(menu_choices))
        #validating user's input
        if result == 1:
             pass
        elif (result == 2) :
            show_menu = False
        else:
             print "WRONG CHOICE"   #EXIT FROM APPLICATION

