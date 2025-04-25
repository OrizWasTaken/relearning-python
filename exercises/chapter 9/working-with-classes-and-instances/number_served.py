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


restaurant = Restaurant('johnbosco', 'shawarma')
msg = f"\n{restaurant.name} has currently served {restaurant.number_served} customers."
print(msg)

# modifying attribute’s value directly through an instance
restaurant.number_served = 500
msg = f"\n{restaurant.name} has currently served {restaurant.number_served} customers."
print(msg)

# modifying attribute’s value through a method
restaurant.set_number_served(620)
msg = f"\n{restaurant.name} has currently served {restaurant.number_served} customers."
print(msg)

# incrementing attribute’s value through a method
restaurant.increment_number_served(25)
msg = f"\n{restaurant.name} has currently served {restaurant.number_served} customers."
print(msg)

