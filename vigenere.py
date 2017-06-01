import sys
from helpers import alphabet_position, rotate_character

def encrypt(message, keyword):
    encrypted_string = ''
    index = 0
    for letter in message:
        #determine the rotation amount from the index of the keyword
        rotation_amount = alphabet_position(keyword[index%len(keyword)])
        #if the key is 'a' or 'A', no rotation
        if rotation_amount == 0:
            encrypted_char = letter
            #check if we had to use a key letter for 0 rotation case
            if letter.lower() in "abcdefghijklmnopqrstuvwxyz":
                index += 1
        else:
            #main encryption
            encrypted_char = rotate_character(letter, rotation_amount)
        #All cases, add to the encrypted string
        encrypted_string += encrypted_char
        #Check if we had a rotation and encryption and burn a key letter
        if encrypted_char != letter:
            index += 1
    return encrypted_string


import unittest

class caesar_tests(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt('The crow flies at midnight!', 'boom'), 'Uvs osck rmwse bh auebwsih!')
        self.assertEqual(encrypt('BaRFoo', 'BaZ'), 'CaQGon')

def validate(cryptokey):
    for element in cryptokey:
        if not element.isalpha():
            bad_key_and_exit()
    return cryptokey

def bad_key_and_exit():
    print("usage: python vigenere.py keyword")
    print("Arguments:")
    print("-keyword : The string to be used as a \"key\" to encrypt your message. Should only contain alphabetic characters-- no numbers or special characters.")
    exit()

def main():
    if len(sys.argv) == 1:
        bad_key_and_exit()
    encryption_key = validate(sys.argv[1])
    print("Type a message")
    message_to_encrypt = input()
    print(encrypt(message_to_encrypt, encryption_key))

if __name__ == "__main__":
#    unittest.main()
    main()