x = str(input())
y = str(input())

n = x.count(y)

if n <= 1 :
    print(x.find(y))
else :
    print(x.find(y), end = ' ')
    print(x.rfind(y))