#my favorite pizza
favorite_pizzas = ["pepperoni", "BBQ chicken", "margherita"]

# print the names of my favorite pizzas
for pizza in favorite_pizzas:
    print(pizza)

print("\n")

# print a sentences using each of my favourite pizzas
for pizza in favorite_pizzas:
    print(f"I crave a slice of {pizza} pizza!")

print("\nI realy love pizza!\n")

# my friends favorite pizza
friend_pizza = favorite_pizzas[:]

# adding new pizzas
favorite_pizzas.append("hawaiian")
friend_pizza.append("veggie")

# proof friend_pizza != favorite_pizza
print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(pizza) 

print("\n")

print("My friend’s favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)