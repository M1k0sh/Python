import re

s = input()

x = re.findall('ab*', s)
print(x)