n = int(input())
rows, cols = (n, n)
arr = [[0 for i in range(cols)] for j in range(rows)]
for i in range(n):
    for j in range(n):
        if i==j:
            arr[i][j] = i*j
        elif i==0:
            arr[i][j] = j
        elif j==0:
            arr[i][j] = i
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()