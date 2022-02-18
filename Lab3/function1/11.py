from re import S

def check(s):
    x = len(s)
    for i in range(len(s)):
        if s[i] != s[x-i-1]:
            return False
            break
    return True

s = input()
print('Palindrome') if check(s) else print('Not Palindrom')