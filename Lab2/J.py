n = int(input())
l = []
for i in range(n):
    s = input()
    cnt1,cnt2,cnt3 = 0,0,0
    for j in range(len(s)):
        if 'a'<=s[j]<='z':
            cnt1+=1
        elif 'A'<=s[j]<='Z':
            cnt2+=1
        elif '0'<=s[j]<='9':
            cnt3+=1
    if cnt1>0 and cnt2>0 and cnt3>0:
        l.append(s)
s = set(l)
l = list(s)
l.sort()
print(len(l))
for word in l:
    print(word)