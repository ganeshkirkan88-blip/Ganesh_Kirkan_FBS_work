# Write a program to enter P, T, R and calculate Compound Interest.

P = int(input('Enter the value of P = '))
R = int(input('Enter the value of R = '))
T = int(input('Enter the value of T = '))

compound_interest = P * ( 1 + R/100 )**T 

print(f'compound_interest is : {compound_interest}')