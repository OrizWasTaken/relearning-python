class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is now open!"
        print(f"\n{msg}")


restaurant = Restaurant('johnbosco', 'shawarma')

print("Name:", restaurant.name)
print("Cuisine Type:", restaurant.cuisine_type)
restaurant.describe_restaurant()