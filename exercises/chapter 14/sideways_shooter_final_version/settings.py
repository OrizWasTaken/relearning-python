class Settings:
    """A class to store all settings for Sideways Shooter."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # ship settings
        self.ships_limit = 3

        # bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (0,0,0)
        self.bullet_limit = 5

        # asteriod settings
        self.asteroid_min_size = 0.1
        self.asteroid_max_size = 0.15

        self.bullet_speed = 5.0

        self.speedup_interval = 10
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.asteroid_speed = 2.0
        self.asteroid_points = 50
        self.asteroid_spawn_interval = 5
        self.ship_speed =3.0

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.asteroid_speed *= self.speedup_scale
        self.asteroid_spawn_interval /= self.speedup_scale
        self.asteroid_points = int(self.asteroid_points * self.speedup_scale)