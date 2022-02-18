def next_3(l):
    for i in range(len(l)-1):
        if l[i] == l[i+1] == 3:
            return True
    return False

l = list(map(int,input().split()))
print(next_3(l))