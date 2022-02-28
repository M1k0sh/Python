n = int(input())

def gen_3_4(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            i+=1
            

g = gen_3_4(n)
for i in g:
    print(i)