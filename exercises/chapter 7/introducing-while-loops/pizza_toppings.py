prompt = "\nWhat topping(s) would you like on your pizza?"
prompt += "\n(Enter 'quit' when you're done)"
print(prompt)

while True:
    topping = input(">>> ")
    if topping == 'quit':
        break
    else: 
        print(f"- I'll add {topping} to your pizza.")



