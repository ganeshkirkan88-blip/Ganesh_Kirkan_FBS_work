#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

S1 =int(input("Enter marks of subject 1:"))
S2 =int(input("Enter marks of subject 2:"))
S3 =int(input("Enter marks of subject 3:"))
S4 =int(input("Enter marks of subject 4:"))
S5 =int(input("Enter marks of subject 5:"))

total_marks = S1 + S2 + S3 + S4 + S5

percentage = total_marks / 5

if(percentage >= 90):
    print('frist class')
elif(percentage >= 70 ):
    print('second class')
elif(percentage >= 50):
    print('third class')
elif(percentage >= 35):
    print('only pass')
else:
    print('Failed...')
