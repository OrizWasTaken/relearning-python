from pathlib import Path
import json

path = Path('favorite_number.json')
favorite_number = input("What's your favorite number? ")
content = json.dumps(favorite_number)
path.write_text(content)

print("Thanks! I'll remember that number.")