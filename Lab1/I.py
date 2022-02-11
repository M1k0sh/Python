x = int(input())
ar = []

for i in range(x) :
    s = str(input())
    ar.append(s)

for i in range(x) :
    if(ar[i].find("@gmail.com") >= 0) :
        k = len(ar[i]) - 10
        print(ar[i].replace("@gmail.com",""))