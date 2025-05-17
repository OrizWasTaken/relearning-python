from pathlib import Path
import json

path = Path('favorite_number.json')

if path.exists():
    content = path.read_text()
    favorite_number = json.loads(content)
    print(f"I know your favorite number!\nIt’s {type(favorite_number)}.")
else:
    favorite_number = input("What's your favorite number? ")
    content = json.dumps(favorite_number)
    path.write_text(content)
    print("Thanks! I'll remember that number.")