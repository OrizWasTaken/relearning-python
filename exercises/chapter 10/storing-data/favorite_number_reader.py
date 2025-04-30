# WARNING: To avoid error, you might have to run 'favorite_number_write.py' at least once before running this file.'

from pathlib import Path
import json
import os

os.chdir('C:/Users/Oriz/Desktop/relearning python/exercises/chapter 10/storing-data')

path = Path('favorite_number.json')

content = path.read_text()
favorite_number = json.loads(content)

print(f"I know your favorite number!\nIt’s {favorite_number}.")