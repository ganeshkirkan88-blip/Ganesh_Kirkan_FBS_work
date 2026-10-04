#Armstrong number 
num=int(input('enter number:'))
temp=num
count=0
while(temp>0):
    count+=1
    temp=temp//10
print(count)
temp=num
sum=0
while(temp>0):
    d=temp%10
    temp=temp//10
    sum=sum+(d**count)   
    print(sum) 
if(sum==num):
    print(f'{num} is an armstrong number.')
else:
    print(f'{num} is not an armstrong number.')