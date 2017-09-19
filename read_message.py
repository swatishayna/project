from select_a_friend import select_a_friend
from steganography.steganography import Steganography
from globals import friends
from select_a_friend import select_a_friend
from datetime import datetime
from steganography.steganography import Steganography
from send_message import New_Chat


def read_message():
    # choose friend from the list
    sender = select_a_friend()

    #New_Chat object
    chat_obj = New_Chat()
    encrypted_image = raw_input("What is the name of the file? ")
    secret_message = Steganography.decode(encrypted_image)
    print secret_message

    chat_obj.message = secret_message
    chat_obj.sent_by_me = False
    #save message
    friends[sender].chats.append(chat_obj)
    print "done"

