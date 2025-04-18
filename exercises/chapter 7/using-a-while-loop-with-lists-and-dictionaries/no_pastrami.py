sandwich_orders = ['tuna', 'pastrami', 'grilled cheese', 'pastrami', 'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("Deli has ran out of pastrami :(\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I'm working on your {current_sandwich} sandwich.")  
    finished_sandwiches.append(current_sandwich)

print('\n')
for finished_sandwich in finished_sandwiches:
    print(f"I've made a {finished_sandwich} sandwich.")

    