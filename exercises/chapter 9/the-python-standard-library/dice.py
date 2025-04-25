from random import randint

class Dice:
    """a simple attempt to model die."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """simulate rolling die."""
        return randint(1, 6)

d6 = Dice()

print("Rolling a dice 10 times:")
print([d6.roll_die() for i in range(10)])