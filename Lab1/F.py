x = int(input())
a = []

for i in range(x) :
    ar = int(input())
    a.append(ar)
    
for i in range(x):
    if a[i] <= 10 :
        print("Go to work!")
    if a[i] > 10 and a[i] <= 25 :
        print("You are weak")
    if a[i] > 25 and a[i] <= 45 :
        print("Okay, fine") 
    if a[i] > 45 :
        print("Burn! Burn! Burn Young!")