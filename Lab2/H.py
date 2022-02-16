from math import sqrt

def closes(l):
    return sqrt((l[0]-x1)**2 + (l[1]-y1)**2)

x1,y1 = map(int,input().split())
n = int(input())
arr = []
for i in range(n):
    l = tuple(map(int,input().split()))
    arr.append(l)
arr.sort(key=closes)

for tup in arr:
    print(tup[0],tup[1])