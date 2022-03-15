import string

def Upper(string):
    cnt = 0
    for i in string:
        if 65 <= ord(i) <= 90:
            cnt += 1
    return cnt

def Lower(string):
    cnt = 0
    for i in string:
        if 97 <= ord(i) <= 122:
            cnt +=1
    return cnt

s = input()

print(f'Upper cases = {Upper(s)}')
print(f'Lower cases = {Lower(s)}')