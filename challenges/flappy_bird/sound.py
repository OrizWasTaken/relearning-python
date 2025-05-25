from pygame.mixer import Sound

class SoundEffect:
    """A class to manage the game's sound effects."""

    def __init__(self):
        """Initialize the sound effects."""
        self.die_sound = Sound('assets/audio/die.wav')
        self.hit_sound = Sound('assets/audio/hit.wav')
        self.point_sound = Sound('assets/audio/point.wav')
        self.wing_sound = Sound('assets/audio/wing.wav')