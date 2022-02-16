l = list(map(str,input().split()))
res = []
for i in range(len(l)):
    s = l[i]
    t = ""
    for j in range(len(s)):
        if not('a'<=s[j].lower()<='z'):
            pass
        else:
            t += s[j]
    res.append(t)
s = set(res)
res = list(s)
res.sort()
print(len(res))
for word in res:
    print(word)