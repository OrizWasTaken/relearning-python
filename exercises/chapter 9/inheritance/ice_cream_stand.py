class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is now open!"
        print(f"\n{msg}")

    def set_number_served(self, value):
        """Resets the value of number_served"""
        self.number_served = value

    def increment_number_served(self, value):
        """Increments the value of number_served"""
        self.number_served += value

# An ice cream stand is a specific kind of restaurant.

class IceCreamStand(Restaurant):
    """A simple attempt to model an ice cream stand"""

    def __init__(self, name, flavors):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(name, cuisine_type='ice cream')
        self.flavors = flavors

    def show_flavors(self):
        """Display available flavors"""
        print(f"\nWe offer {len(self.flavors)} different favors:")
        for flavor in self.flavors:
            print(f"  - {flavor}")

tasty = IceCreamStand('tasty', ['vanila', 'chocolate'])
tasty.describe_restaurant()
tasty.show_flavors()
tasty.open_restaurant()

