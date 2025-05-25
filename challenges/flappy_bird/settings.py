class Settings:
    """A class to store all settings for Flappy Bird."""

    def __init__(self):
        """Initialize the game's settings."""
        self.game_fps = 60
        self.game_speed = 2.5

        # Window settings.
        self.screen_width = 1344
        self.screen_height = 768

        # Bird settings.
        self.bird_acceleration = 0.5
        self.bird_animation_delay = 0.15 # Seconds.
        self.bird_respawn_delay = 2 # Seconds.
        self.jump_force = 7

        # Pipe settings.
        self.pipe_spacing = 285 # Horizontal distance between pipes.
        self.pipe_gap = 130 # Vertical distance between pipes.
        self.first_pipe_delay = 3 # Time delay (seconds) for spawning the first pipe.

        # Scoreboard settings.
        self.bronze_min = 10 # Min score for a bronze medal.
        self.silver_min = 20
        self.gold_min = 30
        self.platinum_min = 40