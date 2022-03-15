from math import prod

def multiply(l):
    return prod(l)

l = list(map(int, input().split()))

print(multiply(l))