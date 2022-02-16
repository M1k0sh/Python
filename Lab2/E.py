s = input()
if not ' ' in s:
    x = int(input())
    n = int(s)
else:
    ind = s.index(' ')
    n = int(s[:ind])
    x = int(s[ind:])

a = [0]*n
res = 0
for i in range(len(a)):
    a[i] = x + 2*i

for i in range(len(a)):
    res = res^a[i]

print(res)


