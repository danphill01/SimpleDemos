from helpers import alphabet_position, rotate_character

def encrypt(test, rot):
    encrypted_string = ''
    for letter in test:
        encrypted_string += rotate_character(letter, rot)
    return encrypted_string


import unittest

class caesar_tests(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt('a', 13), 'n')
        self.assertEqual(encrypt('abcd', 13), 'nopq')
        self.assertEqual(encrypt('LaunchCode', 13), 'YnhapuPbqr')
        self.assertEqual(encrypt('LaunchCode', 1), 'MbvodiDpef')
        self.assertEqual(encrypt('Hello, World!', 5), 'Mjqqt, Btwqi!')

def main():
    print("Do you want to 1) Encrypt or 2) Decrypt?")
    if input() == "1":
        print("Type a message")
        message_to_encrypt = input()
        print("Rotate by:")
        rotation_amount = input()
        print(encrypt(message_to_encrypt, int(rotation_amount)))
    else:
        message_to_decrypt = input("What is the encrypted message")
        for i in range(1,26):
            print(encrypt(message_to_decrypt, i))
            

if __name__ == "__main__":
#    unittest.main()
    main()
