# summing_a_million.py

cubes = [number**3 for number in range(1, 11)]

for cube in cubes:
    print(cube)

# first three elements
print(f"\nThe first three items in the list are: {cubes[:3]}")

# middle three elements
print(f"\nThree items from the middle of the list are: {cubes[4:7]}")

# last three elements
print(f"\nThe last three items in the list are: {cubes[-1:-4:-1]}")