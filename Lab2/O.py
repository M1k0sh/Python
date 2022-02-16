a = ['ZER','ONE','TWO','THR','FOU','FIV','SIX','SEV','EIG','NIN']
b = [0,1,2,3,4,5,6,7,8,9]
s = input()
ind = s.index('+')
deg = (ind/3)-1
num1 = 0
for i in range(0,ind,3):
    for j in range(10):
        if s[i:i+3]==a[j]:
            num1 += b[j]*10**deg
            deg-=1
            break
deg = (len(s)-1-ind)/3-1
num2 = 0
for i in range(ind+1,len(s),3):
    for j in range(10):
        if s[i:i+3]==a[j]:
            num2 += b[j]*10**deg
            deg-=1
            break

ans = round(num1+num2)
t = ""
l = []
while ans!=0:
    l.append(ans%10)
    ans//=10
l.reverse()
for i in range(len(l)):
    for j in range(10):
        if l[i]==b[j]:
            t += a[j]
print(t)