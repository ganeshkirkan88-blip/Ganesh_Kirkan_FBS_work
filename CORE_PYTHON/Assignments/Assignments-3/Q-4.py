#4. Write a program to input all sides of a triangle and check whether triangle is valid or not.
x = int(input('Enter frist triangle:'))
y = int(input('Enter second triangle:'))
z = int(input('Enter third triangle:'))

if(x + y > z and x + z > y and y + z > x): #Sum of two sides should be greater than third side.
    print('triangle is valid')
else:
    print('triangle is not valid')

