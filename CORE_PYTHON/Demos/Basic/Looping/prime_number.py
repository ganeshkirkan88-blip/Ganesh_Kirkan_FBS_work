'''num = int(input("Enter number:"))

for i in range (2,num):
    if(num % i == 0):
        print(f'{num} is not prime number')
        break
else:
    print(f'{num}is a prime number')    '''

#WAP to print prime number between 1 to n   #like(1 to 100)
n = int(input("Enter value of n:"))
for num in range(2,n+1):
    for i in range (2,num):
       if(num % i == 0):
        break
    else:
      print(num,end='_')

#WAP to print frist  n prime number 