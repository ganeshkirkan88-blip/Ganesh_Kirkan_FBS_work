#8. Write a program to convert days into years, weeks and days.
total_days = int(input('enter the total days : '))

year = (total_days // 365) 
weeks = (total_days // 7) 

print(year)
print(weeks)
