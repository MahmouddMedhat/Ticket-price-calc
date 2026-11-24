ticket_price = 100
number_of_tickets = int(input("Enter number of tickets: "))

ticket_price *= number_of_tickets
is_member = input("Are you a member? (yes/no): ")
if is_member in ["yes", "y"]:
    ticket_price *= 0.9
    print(f"Total price = {ticket_price}")
elif is_member in ["no", "n"]:
    print(f"Total price = {ticket_price}")

else:
    print('error')
