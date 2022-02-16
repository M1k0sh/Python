n = int(input())
les = []
res = []
for i in range(n):
   l = list(map(str,input().split()))
   if len(l)>1:
      n = l[0]
      name = l[1]
      les.append(name)
   else:
      n = l[0]
      if len(les)>0:
         res.append(les[0])
         les.remove(les[0])
for s in res:
   print(s,end=' ')