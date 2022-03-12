with open('input1.txt', 'r') as f:
    x = f.read()

cnt = 0
n = x.split('\n')

for i in n:
    if i:
        cnt += 1
print(cnt)