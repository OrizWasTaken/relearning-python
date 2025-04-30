from pathlib import Path
from os import chdir

chdir('C:/Users/Oriz/Desktop/relearning python/exercises/chapter 10/reading-from-a-file/')

path = Path('learning-python.txt')
contents = path.read_text()

print('\nPrinting entire file:')
print(contents)
 

print('\nPrinting file content line-by-line:')
lines = contents.splitlines()
for line in lines:
    print(line)