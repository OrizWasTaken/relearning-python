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


johnbosco = Restaurant('johnbosco', 'Nigerian street food')
johnbosco.describe_restaurant()

ndubisi = Restaurant('ndubisi obeka', 'Nigerian home dishes')
ndubisi.describe_restaurant()

ngozi = Restaurant('ngozi odo', 'Nigerian home dishes')
ngozi.describe_restaurant()

