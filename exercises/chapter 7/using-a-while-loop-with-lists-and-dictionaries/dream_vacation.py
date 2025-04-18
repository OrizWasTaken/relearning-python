places = {}

while True:
    name = input("\nWhat's your name? ")
    place = input(f"Hi, {name.title()}. If you could visit one place in the world, where would you go? ")
    places[name] = place

    repeat = input(f"\nExcellent choice! Would you like to let someone else respond? (yes/no)? ")
    if repeat != 'yes':
        break
    
print("\nAlright. Here are the results of the poll:")
for name, place in places.items():
    print(f"- {name.title()}'s favorite place to visit is {place.title()}.")

