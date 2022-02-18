def unique(l):
    n = []
    for num in l:
        if not num in n:
            n.append(num)
        else:
            pass
    return n

l = list(map(int, input().split()))
print(unique(l))
