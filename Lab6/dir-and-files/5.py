l = ['Geeks','for','Geeks!']
  
with open('input.txt', 'w+') as f:
    for items in l:
        f.write('%s\n' %items)
    print("File written successfully")
f.close()