from pathlib import Path
import json
import os

os.chdir('C:/Users/Oriz/Desktop/relearning python/exercises/chapter 10/storing-data')

def get_new_info(path):
    """Prompt for a new user info"""
    user_info = {
        'first name': input("Whats's your first name? "),
        'last name': input("What's your last name? "),
        'favorite number': input("What's your favorite number? "),
    }
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def get_stored_info(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None  

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    user_info = get_stored_info(path)
    if user_info:
        print(f"Here's what we know about you:")
        for key,value in user_info.items():
            print(f"{key}: {value.title()}")
    else:
        user_info = get_new_info(path)
        print(f"We'll remember you when you come back, {user_info['first name'].title()}!")


greet_user()