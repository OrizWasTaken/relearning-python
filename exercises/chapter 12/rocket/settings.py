class Settings:
    """A class to store all settings for Rocket"""

    def __init__(self):
        """Initialize settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)

        #ship settings
        self.ship_height = 80 # setting
        self.ship_width = 80 
        self.ship_speed = 3