x = input()

sum = 0

for i in range(len(x)):
    s = ord(x[i])
    sum += s
if sum > 300:
    print("It is tasty!")
else:
    print("Oh, no!")