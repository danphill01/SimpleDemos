import string

def translate(text):
    eng2pirate = {'sir':'matey', 'hotel':'fleabag inn', 'student':'swabbie',
                'boy':'matey', 'madam':'proud beauty', 'professor':'foul blaggart',
                'restaurant':'galley', 'your':'yer', 'excuse':'arr',
                'students':'swabbies', 'are':'be', 'lawyer':'foul blaggart',
                'the':'th’', 'restroom':'head', 'my':'me',
                'hello':'avast', 'is':'be', 'man':'matey'}
    new_text = []
    for word in text.split():
        if word in eng2pirate:
            new_text.append(eng2pirate[word])
        else:
            found_punctuation = False
            for index, element in enumerate(word):
                if element in string.punctuation:
#                    print("found punctuation",element,"in",word)
                    new_text.append(translate(word[:index])+element)
                    found_punctuation = True
            if not found_punctuation:
                new_text.append(word)
    return ' '.join(new_text)

text = "hello my man, please excuse your professor to the restroom!"
#testEqual(translate(text), "avast me matey, please arr yer foul blaggart to th' head!")
print(translate(text))

sentence = input("Please enter a sentence for me to translate to Pirate\n")
print(translate(sentence))
