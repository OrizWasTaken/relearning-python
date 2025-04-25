"""a collection of classes related to modeling an admin"""

from user import User

class Admin(User):
    """simple attempt to model an admin account"""
    
    def __init__(self, first_name, last_name, username, email):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an admin.
        """
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()


class Privileges:
    """A class to store and display an admin's privileges."""

    def __init__(self):
         """Initialize attributes of the Privileges class"""
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
