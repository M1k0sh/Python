n = int(input())

def gensquares(m):
    for i in range(1, n+1):
        yield i*i
        i+=1

g = gensquares(n)
for i in g:
    print(i)