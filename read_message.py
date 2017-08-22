from select_a_friend import select_a_friend
from steganography.steganography import Steganography
def read_message() :
    #choose friend from the list
    sender = select_a_friend()

    encrypted_image = raw_input("What is the name of the file? ")
    secret_message = Steganography.decode(encrypted_image)
    print secret_message