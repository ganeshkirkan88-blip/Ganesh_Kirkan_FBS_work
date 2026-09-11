#3. Program to find quotient and remainder of two numbers.

divident = int(input('enter the divident :'))
divisor = int (input ('enter the divisor' ))

if divisor != 0:
    quotient = divident//divisor
    reminder = divident % divisor
print(f'quotient : {quotient}')
print(f'remider : {reminder}')