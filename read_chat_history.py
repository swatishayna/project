from select_a_friend import select_a_friend
from globals import friends
import spy_details
from colorama import init, Fore

spydetails = spy_details
init()

def test():
    print "test called"
    return 0
def read_chat_history():
    print "read called"
    choice = select_a_friend()
    print "selected friend"
    if choice == "error":
        print "read select frind histry cal"
        print Fore.RED + "Wrong choice"+Fore.RESET
    else:
        print "else called"
        print (Fore.BLUE + "Messages sent are shown in blue color \n" + Fore.GREEN + " Received Messages and Read Messages are shown in green color:"+Fore.RESET)
        print "choice atart"
        #choice = int(choice)
        print "choice end"

        chats = friends[choice]
        #chats = friends[choice].get_chats()
        print "chat frind called"
        for chat in chats:
            print "if called"
            if chat['send_by_me']:
                print "if start"
                print (Fore.RED + str(chat['time']) + " " + Fore.BLUE + spydetails.get_name() + " " + Fore.RESET + chat['message'])
                print "if end"
            else:
                print "else called"
                print (Fore.RED + str(chat['time']) + " " + Fore.GREEN + friends[choice].get_name() + " " + Fore.RESET + chat['message'])
                print "else end"
