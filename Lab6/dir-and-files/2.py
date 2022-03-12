import os

path1 = r'C:\Users\PK\python1\Python\Lab6\dir-and-files\input.txt' 

if os.path.exists(path1):
    print("YES")
else:
    print("NO")

if os.path.isdir(path1):
    print("yes")
else:
    print("no")