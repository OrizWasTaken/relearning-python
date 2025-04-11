rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers included in data set:")
for river in rivers: # equivalent to `for river in rivers.keys()`
    print("-", river.title())

print("\nCountries included in data set:")
for country in rivers.values():
    print("-", country.title())