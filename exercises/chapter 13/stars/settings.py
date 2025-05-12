class Settings:
    """A class to store all settings for StarsGame."""

    def __init__(self):
        """Initialize the game's settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)

        # star settings
        self.star_size = (20, 20)