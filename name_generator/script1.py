import random, string


def generator(num):
    vowels='aeiou'
    consonants='bcdfghjklmnpqrxtvwxyz'
    letter=string.ascii_lowercase
    name=''
    for i in range(num):
        letter_input=input("What letter do you want? Enter 'v' for vowel, 'c' for consonant or 'l' for letter: ")
        if letter_input == 'v':
            letter = random.choice(vowels)
        elif letter_input == 'c':
            letter = random.choice(consonants)
        elif letter_input == 'l':
            letter = random.choice(letter)
        else:
            letter = letter_input
        i + 1
        name+=letter

    return name

# print(generator(10))

def name_list(num_names, num):
    for i in range(num_names):
        print(generator(num))


print(name_list(3,8))
