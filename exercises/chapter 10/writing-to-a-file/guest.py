from pathlib import Path
import os

os.chdir('c:/users/oriz/desktop/relearning python/exercises/chapter 10/writing-to-a-file/')

responce = input("Please enter your full name: ")

path = Path('guest.txt')
path.write_text(responce)


