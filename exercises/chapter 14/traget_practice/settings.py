class Settings:
    """A class to store all settings for Target Practice"""

    def __init__(self):
        """Initialize the game's settings."""
        # Game stats
        self.miss_limit = 3

        #  Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        # Ship settings
        self.ship_speed = 5.0

        # Target settings
        self.target_size = (100,100)
        self.target_color = (0,0,0)
        self.target_speed = 1.0
        self.target_direction = 1 # 1 represents down; -1 represents up

        # Bullet settings
        self.bullet_size = (15,3)
        self.bullet_color = (0,0,0)
        self.bullet_speed = 15