l = []
while True:
    n = int(input())
    if n==0:
        break
    l.append(n)
    
if len(l)%2!=0:
    l.insert(round(len(l)/2),0)
res = []
for i in range(round(len(l)/2)):
    res.append(l[i]+l[len(l)-1-i])
for num in res:
    print(num,end=' ')