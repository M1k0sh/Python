def revword(x):
    rev = []
    for i in range(len(x)-1,-1,-1):
        rev.append(x[i])
    return rev

x = list(map(str, input().split()))
m = revword(x)
for words in m:
    print(words, end=' ')