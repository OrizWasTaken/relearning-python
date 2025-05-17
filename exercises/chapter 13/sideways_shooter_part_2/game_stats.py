from settings import Settings

class GameStats:
    """Track statistics for Sideways Shooter 2"""

    def __init__(self):
        """Initialize statistics."""
        self.settings = Settings()
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during"""
        self.ships_left = self.settings.ships_limit
