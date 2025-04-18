prompt = "\nWhat topping(s) would you like on your pizza?"
prompt += "\n(Enter 'quit' when you're done)"
prompt += '\n>>> '

# version 1: use a conditional test in the while statement to stop the loop
topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"- I'll add {topping} to your pizza.")

# version 2: use an active variable to control how long the loop runs.
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else: 
        print(f"- I'll add {topping} to your pizza.")

#version 3: use a break statement to exit the loop when the user enters a 'quit' value.
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else: 
        print(f"- I'll add {topping} to your pizza.")
