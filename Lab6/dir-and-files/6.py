import string

for letter in string.ascii_uppercase:
    with open('{}.txt'.format(letter), 'w') as f:
        f.write(letter)