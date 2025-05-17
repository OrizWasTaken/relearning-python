from settings import Settings

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self):
        """Initialize statistics."""
        self.settings = Settings()
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during"""
        self.misses_left = self.settings.miss_limit