#swap using third variable
x = 10
y = 20 

print(f'Before_swapping x: {x}, y:{y} .')

z = y
y = x
x = z

print(f'After swapping x:{x}, y:{y} .')


#swap without third variable
x = 10
y = 20 

print(f'Before_swapping x: {x}, y:{y} .')

x , y = y , x 

print(f'After swapping x:{x}, y:{y} .')