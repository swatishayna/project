from select_a_friend import select_a_friend
from globals import friends
import spy_details
from colorama import init, Fore

#spydetails = spy_details
init()


def read_chat_history():

    choice = select_a_friend()

    if choice is not None:
        print (Fore.BLUE + "Messages sent are shown in blue color \n" + Fore.GREEN + " Received Messages and Read Messages are shown in green color:"+Fore.RESET)

        chats = friends[choice]['chats']

        for chat in chats:
            if chat['sent_by_me']:
                print (Fore.RED + str(chat['time']) + " " + Fore.BLUE + friends[choice]['name'] + " " + Fore.RESET + chat['message'])
            else:
                print (Fore.RED + str(chat['time']) + " " + Fore.GREEN + friends[choice]['name'] + " " + Fore.RESET + chat['message'])
    else:
        print "Wrong choice"