from pathlib import Path

path = Path('learning-python.txt')
contents = path.read_text()

print('\nPrinting entire file:')
print(contents)
 

print('\nPrinting file content line-by-line:')
lines = contents.splitlines()
for line in lines:
    print(line)