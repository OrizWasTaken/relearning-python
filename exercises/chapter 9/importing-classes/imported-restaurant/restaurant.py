"""a collection of classes related to modeling a restaurant"""

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"\n{self.name} serves wonderful {self.cuisine_type}."
        print(msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"\n{self.name} is now open!"
        print(msg)