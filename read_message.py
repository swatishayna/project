from select_a_friend import select_a_friend
from steganography.steganography import Steganography
from globals import friends
from select_a_friend import select_a_friend
from datetime import datetime
from steganography.steganography import Steganography


def read_message():
    # choose friend from the list
    sender = select_a_friend()

    encrypted_image = raw_input("What is the name of the file? ")
    secret_message = Steganography.decode(encrypted_image)
    print secret_message


    new_chat = {
        "message": secret_message,
        "time": datetime.now(),
        "sent_by_me": False

    }

