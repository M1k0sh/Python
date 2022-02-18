def histogram(l):
    for i in range(len(l)):
        print('*'*l[i])

l = list(map(int, input().split()))
histogram(l)