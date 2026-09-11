#6. Write a Program to input two angles from user and find third angle of the triangle.
Angle1 = int(input('Enter the value of angle 1:'))
Angle2 = int(input('Enter the value of angle 2:'))

third_angle = 180 - ( Angle1 + Angle2 )

print(f'Third angle of trangle is : {third_angle}')