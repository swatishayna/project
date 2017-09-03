from steganography.steganography import Steganography
from select_a_friend import select_a_friend
from datetime import datetime


def send_message():
    # choose a friend from the list
    friend_choice = select_a_friend()

    # prepare the message
    original_image = raw_input("What is the name of the image?")
    output_path = raw_input("Provide name of the output image : ")
    text = raw_input("Enter your message here : ")
    # encrypting the message
    Steganography.encode(original_image , output_path , text)

    # successful message
    print "Your message is encrypted successfully"

    new_chat = {
        "message": text ,
        "time": datetime.now() ,
        "sent_by_me": False

    }
    select_a_friend()[friend_choice]['chats'].append(new_chat)
    print "Your secret message is ready!"
