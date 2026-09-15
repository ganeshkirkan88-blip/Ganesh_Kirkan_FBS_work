#3. Write a program to input angles of a triangle and check whether triangle is valid or not.

x = int(input('Enter the frist angle:'))
y = int(input('Enter the second angle:'))
z = int(input('Enter the third angle:'))

sum= x + y + z
if(sum==180):
    print('triangle is valid')
else:
    print('triangle is invalid')