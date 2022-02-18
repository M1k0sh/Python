def filterprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

l = list(map(int, input().split()))
for j in l:
    if filterprime(j):
        print(j, end=' ')
