x, y = map(int, input().split())

bool = False
for i in range(2, x):
    if x % i == 0:
        bool = True

if x <= 500 and y % 2 == 0 and bool == False:
    print("Good job!")
else :
    print("Try next time!")
