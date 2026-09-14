#if_else condition

#else : block of code execute when above condition becomes false.

#example-1

num = int(input('Enter number'))  
if(num % 2 == 0):
   print(f'{num} is an even number.')
else:
    print(f'{num} is an odd number.')



#example-2
#WAP to print the number is positive or negative.
num = int(input('Enter number'))
if(num > 0):
    print(f'{num} is an positive number.')
else:
    print(f'{num} is an negative number.')

