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

class Admin(User):
    """simple attempt to model an admin account"""
    
    def __init__(self, first_name, last_name, username, email):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an admin.
        """
        super().__init__(first_name, last_name, username, email)
        self.privileges = [
            'can reset passwords',
            'can moderate discussions',
            'can suspend accounts',
            ]

    def show_privileges(self):
        """Display admin privileges"""
        print('privileges:')
        for privilege in self.privileges:
            print(f"- {privilege}")

joseph = Admin('joseph', 'orisakwe', 'oriz4life', 'oriz4life2022@gmail.com')
joseph.greet_user()
joseph.show_privileges()