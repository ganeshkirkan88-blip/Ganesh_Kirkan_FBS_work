#8. Write a program to prompt user to enter userid and password. After verifying
#userid and password display a 4 digit random number and ask user to enter the same.
#If user enters the same number then show him success message otherwisefailed. (Something like captcha)

user_id = input('Enter your user ID: ')
password = input('Enter your password: ')
captcha = input('Enter the captcha: ')
if user_id == 'ganesh' and password == '1234':
    if captcha == 'ABCD':
        print('Login successful.')
    else:
        print('Invalid captcha.')
else:
    print('Invalid user ID or password.')