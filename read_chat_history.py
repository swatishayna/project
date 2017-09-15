from select_a_friend import select_a_friend
from globals import friends
import spy_details
from colorama import init, Fore

spydetails = spy_details
init()


def read_chat_history():
    choice = select_a_friend()
    if choice == "error":
        print Fore.RED+"Wrong choice"+Fore.RESET
    else:
        print (Fore.BLUE + "Messages sent are shown in blue color \n" + Fore.GREEN + " Received Messages and Read Messages are shown in green color:"+Fore.RESET)
        choice = int(choice)
        chats = friends[choice].get_chats()
        for chat in chats:
            if chat['send_by_me']:
                print (Fore.RED + str(chat['time']) + " " + Fore.BLUE + spydetails.get_name() + " " + Fore.RESET + chat['message'])
            else:
                print (Fore.RED + str(chat['time']) + " " + Fore.GREEN + friends[choice].get_name() + " " + Fore.RESET + chat['message'])
