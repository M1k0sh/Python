# Function to find permutations of a given string
from itertools import permutations

def tolist(s):
    l = []
    for letter in s:
        l.append(letter)
    return l

def purmm(l):
    perm = list(permutations(l))
    for tup in perm:
        for let in tup:
            print(let,end='')
        print()


s = input()
l = tolist(s)
purmm(l)