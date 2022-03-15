from math import sqrt
import time

def square_root(x, y):
    time.sleep(y / 1000)
    return sqrt(x)

x = int(input())
y = int(input())

print(f'Square root of {x} after {y} miliseconds is {square_root(x, y)}')