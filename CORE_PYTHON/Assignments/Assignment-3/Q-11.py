#11. Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

total_amount = 0
for i in range(1,6):
    age = int(input('Enter the age of person : '))
    ticket_amount = float(input('Enter the ticket amount of person : '))

    if age < 12:
        discount = 0.3 * ticket_amount
    elif age > 59:
        discount = 0.5 * ticket_amount
    else:
        discount = 0

    total_amount += (ticket_amount - discount)

print(f"Total amount to be paid for all persons: {total_amount}")