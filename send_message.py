from steganography.steganography import Steganography
from select_a_friend import select_a_friend
from datetime import datetime
from globals import friends
from colorama import Fore, init
from main import si
#import spy_info_class
init()

# saving the messages
class New_Chat :
    message = ''
    time = datetime.now()
    sent_by_me = True

def send_message():
    chat_obj = New_Chat()
    # choose a friend from the list
    friend_choice = select_a_friend()

    if friend_choice is not None:
        # prepare the message
        original_image = raw_input("What is the name of the image?")
        output_path = raw_input("Provide name of the output image : ")
        text = raw_input("Enter your message here : ")
        # encrypting the message
        Steganography.encode(original_image, output_path, text)
        # successful message
        print "Your message is encrypted successfully"

        chat_obj.message = text

        #  save message
        si.chats.append(chat_obj)
        print " done"
    else:
        print "wrong choice"