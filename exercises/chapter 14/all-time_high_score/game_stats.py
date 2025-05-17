from pathlib import Path
import json

class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.path = Path('user_data.json')

        # read high score, if any; else initialize high score
        if self.path.exists():
            self.read_highscore()
        else:
            self.high_score = 0

        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_highscore(self):
        """Save high score to a .json file"""
        content = json.dumps(self.high_score)
        self.path.write_text(content)

    def read_highscore(self):
        """Read high score from a .json file"""
        content = self.path.read_text()
        self.high_score = json.loads(content)
        