from settings import Settings

class GameStats:
    """Track statistics for Sideways Shooter 2"""

    def __init__(self, ss_game):
        """Initialize statistics."""
        self.settings = ss_game.settings
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during"""
        self.ships_left = self.settings.ships_limit
        self.score = 0