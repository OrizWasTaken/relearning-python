class Settings:
    """A class to store all settings for Sideways Shooter."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # ship settings
        self.ship_speed = 5
        self.ships_limit = 3

        # bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (0,0,0)
        self.bullet_limit = 5

        # asteriod settings
        self.asteroid_speed = 5
        self.asteroid_spawn_delay = 80
        self.asteroid_min_size = 0.1
        self.asteroid_max_size = 0.15