import re

txt = input()

x = re.findall("a*b{2,3}", txt)

print(x)