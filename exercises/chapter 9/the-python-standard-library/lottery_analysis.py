from random import choice

def get_ticket(possibilities):
    """create a winning ticket of 4 numbers, letters or both"""
    winning_ticket = []
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket

possibilities = [1, 2, 3, 4, 5, 6, 7, 0, 9, 10, 'g', 'b', 'c', 'd', 'h']

# getting winning ticket
winning_ticket = get_ticket(possibilities)
print(f"The final winning ticket is: {winning_ticket}")

# check how many plays it takes to win
play = True
plays = 0
while play:
    plays += 1
    random_ticket = get_ticket(possibilities)
    if set(random_ticket) == set(winning_ticket) or plays == 1_000_000:
        play = False
    
print(f"\nYour winning ticket is: {random_ticket}")
print(f"It took you {plays} tries to win.")
