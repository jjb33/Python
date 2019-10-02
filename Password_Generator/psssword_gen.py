'''
password generator, written from scratch. Must be a minimum of 8 characters, and the result will include one each of uppercase,
lowercase, number, and punctuation.
'''

import string
import random

#Make sure we are meeting the required length and input is correct data type (integer)

while True:
    inp = input('How long of a password do you want minimum of 8)?')
    try:
        int(inp)
    except:
        print('Make sure you have a whole number that is 8 or greater!')
        continue
    if int(inp) <= 8:
        print('That is not 8 or greater!')
        continue
    if int(inp) > 100:
        print('Let\'s keep it 100 characters or less') #Sometimes may want a long one to put into a password manager?
        continue
    else:
        inp = int(inp)
    break

def passgen(char_count):
    nums = list(string.digits)
    letters_lower = list(string.ascii_lowercase)
    letters_upper = list(string.ascii_uppercase)
    punct = list(string.punctuation)

    char_pool = [nums, letters_lower, letters_upper, punct]

    for list_of_chars in char_pool:
        random.shuffle(list_of_chars)

    i = 1
    password = []
    for lists in range(0, 4):
        x = str(char_pool[lists][random.randint(0, (len(char_pool[lists]) - 1))])
        password.append(x)
        i += 1
    while i <= char_count:
        random.shuffle(char_pool)
        x = str(char_pool[0][random.randint(0, (len(char_pool[0]) - 1))])
        password.append(x)
        i += 1
    random.shuffle(password)
    password = ''.join(password)
    print(password)
    return password
    
passgen(inp)

        
        
