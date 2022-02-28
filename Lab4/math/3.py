from math import tan, pi

num = int(input('Input number of sides: '))
length = int(input('Input the length of a side: '))

area = num * (length ** 2) / (4 * tan(pi / num))

print('The area of the polygon is:', int(area))