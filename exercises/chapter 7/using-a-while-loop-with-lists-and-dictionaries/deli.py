sandwich_orders = ['tuna', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I'm working on your {current_sandwich} sandwich.")  
    finished_sandwiches.append(current_sandwich)

print('\n')
for finished_sandwich in finished_sandwiches:
    print(f"I've made a {finished_sandwich} sandwich.")

    