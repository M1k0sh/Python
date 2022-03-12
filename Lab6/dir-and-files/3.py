import os
path = r'C:\Users\PK\python1\Python\Lab6\dir-and-files\input.txt'
print(os.path.exists(path))

path = r'C:\Users\PK\python1\Python\Lab6\dir-and-files\input1.txt'
print(os.path.exists(path))

print("\nFile name of the path:")
print(os.path.basename(path))

print("\nDir name of the path:")
print(os.path.dirname(path))