from pathlib import Path

responce = input("Please enter your full name: ")

path = Path('guest.txt')
path.write_text(responce)


