#7. Program to Find the Roots of a Quadratic Equation

a = int(input('enter the value of a : '))
b = int(input('enter the value of b : '))
c = int(input('enter the value of c : '))

d = (b**2) - (4*a*c)

X1 = (-b + (d**0.5)) / (2* a)
X2 = (-b - (d**0.5) )/ (2* a)

print(f'root is : {X1}')
print(f'root is : {X2}')