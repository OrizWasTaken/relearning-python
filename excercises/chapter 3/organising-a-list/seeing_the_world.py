locations = ["usa", "paris", "london", "australia", "canada"]

print("\noriginal order:")
print(locations)

# visit list in alphabetical order
print("\nalphabetical order:")
print(sorted(locations))

# visit list in original order
print("\noriginal order:")
print(locations)

# visit list in reverse-alphabetical order
print("\nreverse-alphabetical order:")
print(sorted(locations, reverse=True))

# visit list in original order
print("\original order:")
print(locations)

# visit list in reversed order
locations.reverse()
print("\nreversed order:")
print(locations)

# visit list in original order
locations.reverse()
print("\noriginal order:")
print(locations)

# visit list in alphabetical order
locations.sort()
print("\nalphabetical order:")
print(locations)

# visit list in reverse-alphabetical order
locations.sort(reverse=True)
print("\nreverse-alphabetical order:")
print(locations)