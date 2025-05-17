class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 810
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 5

        # Alien settings
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # fleet_direction of 1 represents right; -1 represents left.

        # Default button settings
        self.button_size = (200, 50)
        self.base_color = (0, 135, 0)
        self.highlighted_color = (135, 0, 0)
        self.button_text_color = (255, 255, 255)
        self.button_font_size = 48

        # How quickly the game speeds up
        self.speedup_scale = 1.2

        self.difficulty_level = 'medium'

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        if self.difficulty_level == 'easy':
            self._easy_difficulty()
        elif self.difficulty_level == 'medium':
            self._meduim_difficulty()
        elif self.difficulty_level == 'hard':
            self._hard_difficuly()

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

    def _easy_difficulty(self):
        """Initialize settings to easy mode"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

    def _meduim_difficulty(self):  
        """Initialize settings to medium mode"""
        self.ship_speed = 2.5
        self.bullet_speed = 3.5
        self.alien_speed = 2.0
    
    def _hard_difficuly(self):
        """Initialize settings to hard mode"""
        self.ship_speed = 3.5
        self.bullet_speed = 4.0
        self.alien_speed = 3.0