from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path('cats.txt')
    print(f'\nReading file: {filename}')
    try:
        content = path.read_text()
    except FileNotFoundError:
        print("Sorry, I can't find that file.")
    else:
        print(f'{content}')