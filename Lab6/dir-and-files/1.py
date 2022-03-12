import os

path1 = r'C:\Users\PK\python1\Python\Lab6\dir-and-files' 

directories = os.listdir(path1)

for file in directories:
    print(file)