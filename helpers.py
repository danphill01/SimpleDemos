def alphabet_position(letter):
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    return alpha_lower.find(letter.lower())

def rotate_character(char, rot):
    #Test if in lower case chars first
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    position = alphabet_position(char)
    if position < 0:
        #not a alpha char, so return the char
        return char
    else:
        if char in alpha_lower:
            #perform the lower case rotation
            return alpha_lower[(position+rot)%26]
        else:
            #perform the upper case rotation
            return alpha_lower[(position+rot)%26].upper()

import unittest

class caesar_tests(unittest.TestCase):

    def test_alphabet_position(self):
        self.assertEqual(alphabet_position('a'), 0)
        self.assertEqual(alphabet_position('A'), 0)
        self.assertEqual(alphabet_position('b'), 1)
        self.assertEqual(alphabet_position('y'), 24)
        self.assertEqual(alphabet_position('z'), 25)
        self.assertEqual(alphabet_position('Z'), 25)

    def test_rotate_character(self):
        self.assertEqual(rotate_character('a', 13), 'n')
        self.assertEqual(rotate_character('a', 14), 'o')
        self.assertEqual(rotate_character('a', 0), 'a')
        self.assertEqual(rotate_character('c', 26), 'c')
        self.assertEqual(rotate_character('c', 27), 'd')
        self.assertEqual(rotate_character('A', 13), 'N')
        self.assertEqual(rotate_character('z', 1), 'a')
        self.assertEqual(rotate_character('Z', 2), 'B')
        self.assertEqual(rotate_character('z', 37), 'k')
        self.assertEqual(rotate_character('!', 37), '!')
        self.assertEqual(rotate_character('6', 13), '6')

if __name__ == "__main__":
    unittest.main()
