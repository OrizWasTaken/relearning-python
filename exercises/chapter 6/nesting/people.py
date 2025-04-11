people = []

person = {
    'first': 'david',
    'last': 'orisakwe',
    'age': 23,
    'country': 'united states',
}
people.append(person)

person = {
    'first': 'michael',
    'last': 'orisakwe',
    'age': 21,
    'country': 'nigeria',
}
people.append(person)

person = {
    'first': 'joseph',
    'last': 'orisakwe',
    'age': 19,
    'country': 'nigeria',
}
people.append(person)

person = {
    'first': 'franklyn',
    'last': 'orisakwe',
    'age': 17,
    'country': 'nigeria',
}
people.append(person)

for person in people:
    name = f"{person['first']} {person['last']}".title()
    age = person['age']
    country = person['country'].title()

    print(f"{name}, aged {age}, is currently in {country}.")
    