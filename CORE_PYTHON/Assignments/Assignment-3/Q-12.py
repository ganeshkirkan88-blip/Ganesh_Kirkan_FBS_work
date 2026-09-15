# 12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter the three number :'))
temp = num
rev_num = 0
while(temp > 0):
    d = temp % 10
    temp =temp //10
    rev_num = rev_num * 10 + d
if(rev_num == num):
    print('The number is pallindrome.')
else:
    print('The number is not pallindrome.')
    
