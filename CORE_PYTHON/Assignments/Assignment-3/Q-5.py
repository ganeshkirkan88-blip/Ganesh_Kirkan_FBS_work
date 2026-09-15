#5.Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

x = int(input('Enter frist triangle:'))
y = int(input('Enter second triangle:'))
z = int(input('Enter third triangle:'))

if(x == y & y == z):
    print('trisngle is equilateral.')
elif(x == y or y == z or x == z):
    print('triangle is isosceles.')
else:
    print('triangle is scalene')