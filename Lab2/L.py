s = input()
l = []
for i in range(len(s)):
    if s[i]=='(' or s[i]=='[' or s[i]=='{':
        l.append(s[i])
    else:
        ok = True
        if len(l)!=0:
            if l[len(l)-1]=='(' and s[i]==')':
                l.pop()
            elif l[len(l)-1]=='{' and s[i]=='}':
                l.pop()
            elif l[len(l)-1]=='[' and s[i]==']':
                l.pop()
            else:
                ok = False
                break
        else:
            ok = False
            break
if len(l)==0:
    print('Yes')
else:
    print('No')