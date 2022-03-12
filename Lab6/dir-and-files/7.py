with open('first.txt','r') as first, open('second.txt','a') as second:
    for line in first:
            #append content to second file
            second.write(line)