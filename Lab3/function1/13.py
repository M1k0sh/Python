import random

print("Hello! What is your name?")
name = input()
print()
print(f'Well, {name}, I am thinking of a number between 1 and 20.')
print("Take a guess.")

k = random.randrange(1,20)
x=-1
sum=0

while x != k:
    n = int(input())
    print()
    if n < k:
        print('Your guess is too low.')
        print("Take a guess.")
    else:
        print('Your guess is too bigger.')
        print("Take a guess.")
    x=n
    sum+=1
print(f'Good job, {name}! You guessed my number in {sum} guesses!')