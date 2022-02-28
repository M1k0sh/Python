a = int(input())
b = int(input())

def gensquares(b):
    for i in range(a, b+1):
        yield i*i
        i+=1
            

g = gensquares(b)
for i in g:
    print(i)