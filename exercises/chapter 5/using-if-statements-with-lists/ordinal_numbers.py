numbers = list(range(10))

for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    elif number > 3:
        print(f'{number}th')