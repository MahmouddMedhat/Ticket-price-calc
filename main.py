ticket_price = 100
number_of_tickets=""

while not number_of_tikets.isnumeric():
   number_of_tickets = input("Enter number of tickets:")

number_of_tickets = int(number_of_tickets)

ticket_price *= number_of_tickets
if ticket_price>=1000:
    ticket_price*=0.8
else:
   is_member = input("Are you a member? (yes/no): ")

   if is_member in ["yes", "y"]:
    ticket_price *= 0.9
    
print(f"Total price = {ticket_price}")
