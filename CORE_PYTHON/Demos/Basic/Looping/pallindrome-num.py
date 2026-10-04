#
n= int(input('Enter the number:'))
temp = n
rev_num = 0
while(n > 0):
    d=temp%10
    temp=temp//10
    rev_num=rev_num*10+d
    if(rev_num == n):
        print('the number is pallindrome.')
    else:
        print('the number is not pallindrome.')