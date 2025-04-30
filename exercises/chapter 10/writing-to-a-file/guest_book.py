from pathlib import Path
import os

os.chdir('c:/users/oriz/desktop/relearning python/exercises/chapter 10/writing-to-a-file/')

guest = ""
numbering = 0
while True:
    prompt = "\nPlease enter your full name"
    prompt += ("\n(Enter 'q' to quit): ")

    responce = input(prompt)
    if responce == 'q':
        break
    numbering += 1
    guest += f"{numbering}.\t{responce}\n"

path = Path('guest.txt')
path.write_text(guest)