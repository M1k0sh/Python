n = int(input())

def decrease(n):
    for i in range(n):
        yield n
        n-=1

g = decrease(n)

for i in g:
    print(i)