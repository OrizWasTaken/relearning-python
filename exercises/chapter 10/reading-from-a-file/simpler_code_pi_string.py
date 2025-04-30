from pathlib import Path
from os import chdir

chdir('C:/Users/Oriz/Desktop/relearning python/exercises/chapter 10/reading-from-a-file/')

path = Path('pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))