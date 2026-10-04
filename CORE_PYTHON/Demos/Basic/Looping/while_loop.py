
#syntax:-
#while(condition): 
    #block of code
##loop will  excute if conditon is true when condition becomes false then it will stop


#variable:
           #1.Initialization 
           #2.used in condition 
           #3.valuse should be change (increment/decrement)




#i = 0          #variable initialization
#while(i < 5):        #used in condition 
#    print('Hello World!')
 #   i += 1   #i = i + 1 #value should be change



#example

#i = 1
#while(i<=10):
 #  print(i)
  # i += 1



num = int(input('Enter number : '))
i=1
while(i<=10):
    print(f'{num}*{i}={num*i}')
    i+=1