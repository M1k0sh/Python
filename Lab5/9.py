import re

txt = input()

print(re.sub(r"(\w)([A-Z])", r"\1 \2", txt))