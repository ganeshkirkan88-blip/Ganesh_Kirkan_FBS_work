#6. Write a program to calculate profit or loss.

CP = int(input('Enter Cost Price: '))
SP = int(input('Enter Selling Price: '))

if(SP > CP):
    profit = SP - CP
    print('Profit =', profit)
elif(CP > SP):
    loss = CP - SP
    print('Loss =', loss)