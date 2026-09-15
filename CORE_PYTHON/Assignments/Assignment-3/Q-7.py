#7. Write a program to check if user has entered correct userid and password.

user_id = input('Enter user id :' )
password = input('Enter user password :')

if(user_id == 'ganesh'and password == '1234'):
    print('Login successfully')
else:
    print('wrong user_id and password')
