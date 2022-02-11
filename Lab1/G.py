s = str(input())

sum = 0

x = len(s)

f = x - 1

m = 0

for i in range(x):
    p = int(s[i])*(2**f)
    f = f - 1
    m += p
print(m)