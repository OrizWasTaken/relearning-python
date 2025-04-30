from pathlib import Path
from os import chdir

chdir('C:/Users/Oriz/Desktop/relearning python/exercises/chapter 10/reading-from-a-file/')

path = Path('pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
  print(line)