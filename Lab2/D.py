n = int(input())
rows, cols = (n, n)
arr = [['.' for i in range(cols)] for j in range(rows)]
for i in range(n):
    for j in range(n):
        if n%2!=0:
            if i+j>=n-1:
                arr[i][j] = '#'
        else:
            if i>=j:
                arr[i][j] = '#'

for i in range(n):
    for j in range(n):
        print(arr[i][j],end='')
    print()
