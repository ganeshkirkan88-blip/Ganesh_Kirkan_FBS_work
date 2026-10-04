# WAP to check given number is strong or not
num=int(input('Enter  the number :'))
temp=num
sum=0
while(temp>0):
    d=temp%10
    temp = temp//10
    fact=1
    for i  in range(1,d+1):
        fact = fact*i
    sum = sum +fact
if(sum == num):
    print('the number is strong.')
else:
    print('the number is not strong.')    
