import re

x = input()
snake = re.sub('_', x).lower()

print(snake)