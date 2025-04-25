from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 0, 9, 10, 'g', 'b', 'c', 'd', 'h']
print("Let's see what the winning ticket is...")

winning_ticket = []
while len(winning_ticket) < 5:
    pulled_item = choice(possibilities)
    if pulled_item not in winning_ticket:
        print(f"  We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)

print(f"\nThe final winning ticket is: {winning_ticket}")