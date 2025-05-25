from pathlib import Path
import json

class GameStats:
    """A class to manage the game statistics."""

    def __init__(self, fb_game):
        """Initialize the GameStats atttributes."""
        self.sound = fb_game.sound
        self.reset_score()
        self.path = Path('high_score.json')

        # Load high score from path, if exits.
        # Else zero high score.
        if self.path.exists():
            self.high_score = self.load_high_score()
        else:
            self.high_score = 0

    def reset_score(self):
        """Reset the player's score."""
        self.score = 0
        self.high_score_broken = False

    def update(self):
        """Update the player's current score and high score."""
        self.score += 0.5
        self.sound.point_sound.play()

        # Update high score, if surpassed.
        if self.score > self.high_score:
            self.high_score_broken = True
            self.high_score = self.score

    def save_high_score(self):
        """Write the high score to a path."""
        content = json.dumps(self.high_score)
        self.path.write_text(content)

    def load_high_score(self):
        """Read the high score from a path."""
        content = self.path.read_text()
        return json.loads(content)