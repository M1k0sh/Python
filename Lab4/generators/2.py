n = int(input())

def geneven(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
            i+=1
            

g = geneven(n)
for i in g:
    print(i)