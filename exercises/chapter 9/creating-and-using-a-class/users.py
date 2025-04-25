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


oriz4life = User('joseph', 'orisakwe', 'oriz4life', 'oriz4life2022@gmail.com')
oriz4life.describe_user()
oriz4life.greet_user()

yungthirsty = User('david', 'orisakwe', 'yungthirsty', 'yungthirsty2019@gmail.com')
yungthirsty.describe_user()
yungthirsty.greet_user()

mangoman = User('franklyn', 'orisakwe', 'mangoman', 'mangoman111@gmail.com')
mangoman.describe_user()
mangoman.greet_user()