# 5-2: More Conditional Tests

# 1. Tests for equality and inequality with strings
color = 'Red'
print("Is color == 'Red'? I predict True.")
print(color == 'Red')

print("\nIs color != 'Blue'? I predict True.")
print(color != 'Blue')

print("\nIs color == 'blue'? I predict False.")
print(color == 'blue')

# 2. Tests using the lower() method
print("\nIs color.lower() == 'red'? I predict True.")
print(color.lower() == 'red')

print("\nIs color.lower() == 'Red'? I predict False.")
print(color.lower() == 'Red')

# 3. Numerical tests
age = 21
print("\nIs age == 21? I predict True.")
print(age == 21)

print("\nIs age != 30? I predict True.")
print(age != 30)

print("\nIs age > 18? I predict True.")
print(age > 18)

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs age >= 21? I predict True.")
print(age >= 21)

print("\nIs age <= 20? I predict False.")
print(age <= 20)

# 4. Tests using and / or
score = 85
print("\nIs age > 18 and score > 80? I predict True.")
print(age > 18 and score > 80)

print("\nIs age < 18 or score > 80? I predict True.")
print(age < 18 or score > 80)

print("\nIs age < 18 and score < 80? I predict False.")
print(age < 18 and score < 80)

# 5. Test whether an item is in a list
fruits = ['apple', 'banana', 'mango']
print("\nIs 'banana' in fruits? I predict True.")
print('banana' in fruits)

print("\nIs 'grape' in fruits? I predict False.")
print('grape' in fruits)

# 6. Test whether an item is not in a list
print("\nIs 'grape' not in fruits? I predict True.")
print('grape' not in fruits)

print("\nIs 'apple' not in fruits? I predict False.")
print('apple' not in fruits)
