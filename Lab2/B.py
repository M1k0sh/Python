x = int(input())
a = list(map(int,input().split()))

a.sort()

print(a[x-1]*a[x-2])