from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.start_x, self.start_y = (0,0)
        self.x_values = [self.start_x]
        self.y_values = [self.start_y]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Get steps.
            x_step = self._get_step()
            y_step = self._get_step()

            # Reject moves that go nowhere.
            if not x_step and not y_step:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

            self.end_x, self.end_y = (
                self.x_values[-1], self.y_values[-1])
            
    def _get_step(self):
        "Determine the direction and distance for each step"
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return  direction * distance