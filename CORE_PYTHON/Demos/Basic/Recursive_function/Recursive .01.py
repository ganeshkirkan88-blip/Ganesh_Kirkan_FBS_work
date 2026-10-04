#
def series(n):     #Function call itself inside the function 
    if(n>0):
        print(n)
        series(n-1)

n = 5
series(n)

# to print 1 to 10 number using recursion function
def print_numbers(n):
    if(n > 10):
      return
    print(n)
    print_numbers(n + 1)
print_numbers(1)