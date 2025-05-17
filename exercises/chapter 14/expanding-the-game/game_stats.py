from pathlib import Path
import json

class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings

        # Create path object to read and save high score.
        self.path = Path('user_data/high_score.json')

        self.high_score = self.get_high_score()
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Save high score to path."""
        content = json.dumps(self.high_score)
        self.path.write_text(content)

    def get_high_score(self):
        """Return high score from path, if any; else 0."""
        if self.path.exists():
            content = self.path.read_text()
            return json.loads(content)
        return 0

