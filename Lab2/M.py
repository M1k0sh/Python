l = []
while True:
    s = input()
    t = ''
    if s!='0':
        sd = s[:2]
        sm = s[3:5]
        sy = s[6:]
        t += sy + ' ' + sm + ' ' + sd
        l.append(t)
    else:
        break
l.sort()
for string in l:
    y = string[:4]
    m = string[5:7]
    d = string[8:]
    print(d,m,y)