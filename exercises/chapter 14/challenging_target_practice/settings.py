class Settings:
    """A class to store all settings for Target Practice"""

    def __init__(self):
        """Initialize the game's settings."""
        # Game stats
        self.miss_limit = 10

        #  Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        # Target settings
        self.target_size = (100,100)
        self.target_color = (0,0,0)

        # Bullet settings
        self.bullet_size = (15,3)
        self.bullet_color = (0,0,0)
        self.bullet_speed = 15

        # How quickly the game speeds up
        self.speedup_scale = 1.0005

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # Ship settings
        self.ship_speed = 3

        # Target settings
        self.target_speed = 1.0
        self.target_direction = 1 # 1 represents down; -1 represents up

        # Bullet setting
        self.bullet_speed = 10
        

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale