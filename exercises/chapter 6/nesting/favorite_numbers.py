favorite_num = {
    'joe': [19, 6, 10, 23],
    'dave': [23, 7, 1],
    'mike': [2, 18, 6],
    'frank': [17, 12],
}

for name, numbers in favorite_num.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print("-", number)
