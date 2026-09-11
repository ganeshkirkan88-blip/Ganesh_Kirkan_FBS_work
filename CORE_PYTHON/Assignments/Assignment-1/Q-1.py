#1. Write a program to calculate the percentage of student based on marks of any 5
    #subjects.

sub1 = int (input('enter the subject one mark : '))
sub2 = int (input('enter the subject two mark : '))
sub3 = int (input('enter the subject three mark : '))
sub4 = int (input('enter the subject four mark : '))
sub5 = int (input('enter the subject five mark : '))
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
per = (total_marks / 500 ) * 100
print(f'percentage of  five sub is {per}.')