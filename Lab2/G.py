n = int(input())
demon = dict()
for i in range(n):
    name,weak = map(str,input().split())
    if not weak in demon:
        demon[weak] = 1
    else:
        demon[weak] += 1

m = int(input())
hun = dict()
for i in range(m):
    name, power, quan = map(str,input().split())
    if not power in hun:
        hun[power] = int(quan)
    else:
        hun[power] += int(quan)
    
sum = 0
for power in hun.keys():
    for weak in demon.keys():
        if power==weak:
            if hun[power]-demon[weak]>=0:
                sum += demon[weak]
            else:
                sum = sum + hun[power]

print(f'Demons left: {n-sum}')