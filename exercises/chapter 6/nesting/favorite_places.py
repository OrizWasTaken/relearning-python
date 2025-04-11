favorite_places = {
    'david': ['paris', 'los angeles', 'london'],
    'michael': ['london', 'rome', 'dubia'],
    'franklyn': ['new york', 'barcelona', 'paris', 'switzerland']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places to visit are:")
    for place in places:
        print(f"- {place.title()}")