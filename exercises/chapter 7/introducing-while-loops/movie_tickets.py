prompt = "\nHow old are you?"
prompt += "\n(Enter 'quit' when you are finished) "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)

    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    elif age > 12:
        price = 15
    
    print(f"Your ticket is ${price}.")