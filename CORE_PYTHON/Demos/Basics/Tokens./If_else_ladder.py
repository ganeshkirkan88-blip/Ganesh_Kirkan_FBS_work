#
num = int(input('Enter number:'))
if(num == 0):
    print('the number is neutral.')
elif(num>0):
    print('the number is positive.')
else:
    print('the number is negative.')    

## 
a = 10
b = 20
c = 15

if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")
