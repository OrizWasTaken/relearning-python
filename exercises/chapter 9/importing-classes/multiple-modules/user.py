"""a collection of classes related to modeling a user"""

class User:
    """simple attempt to model a user account"""

    def __init__(self, first_name:str, last_name:str, username:str, email:str):
        """Initialize user"""
        self.first = first_name
        self.last = last_name
        self.username = username
        self.email = email
        self.followers = 0
        self.following = 0
        self.login_attempts = 0

    def describe_user(self):
        """Display user summary"""
        print("\nYour profile:")
        print(f"\t- username: {self.username}")
        print(f"\t- email: {self.email}")
        print(f"\t- full name: {self.first.title()} {self.last.title()}")
        print(f"\t- followers: {self.followers}")
        print(f"\t- following: {self.following}")

    def greet_user(self):
        """Displays a greeting to user"""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login_attempts."""
        self.login_attempts = 0