pets = []

pet = {
    'name': 'kilian',
    'kind': 'cat',
    'owner': 'dave',
}
pets.append(pet)

pet = {
    'name': 'brave',
    'kind': 'dog',
    'owner': 'mike',
}
pets.append(pet)

pet = {
    'name': 'pen',
    'kind': 'chicken',
    'owner': 'frank',
}
pets.append(pet)


for pet in pets:
    print(f"{pet['name'].title()} is {pet['owner'].title()}'s {pet['kind']}.")
    
    
    