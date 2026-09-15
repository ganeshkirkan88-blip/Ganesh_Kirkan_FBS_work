#2. Write a program to input any alphabet and check whether it is vowel or consonant.

char = input('Enter the charecter:')

if(char in 'aeiouAEIOU'):
   print(f'{char} is vowel.')
else:
   print(f'{char} is constant.')
