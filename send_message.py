from steganography.steganography import Steganography
from select_a_friend import select_a_friend
from datetime import datetime
from globals import friends
from colorama import Fore, init
import spy_info_class

init()
def send_message():
    # choose a friend from the list
    friend_choice = select_a_friend()
    if (friend_choice == "error"):
        print Fore.RED + "wrong choice" + Fore.RESET
    else:
        friend_choice = (select_a_friend())

        # prepare the message
        original_image = raw_input("What is the name of the image?")
        output_path = raw_input("Provide name of the output image : ")
        text = raw_input("Enter your message here : ")
        # encrypting the message
        Steganography.encode(original_image, output_path, text)

            # successful message
        print "Your message is encrypted successfully"

    # saving the messages
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True

    }

    friends[friend_choice].append(new_chat)
    print "Your secret message is ready!"
