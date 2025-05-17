import pygame
import random
from pygame.sprite import Sprite

class Asteroids(Sprite):
    """A class to represent a single asteroid."""

    def __init__(self, ss_game):
        """Initialize the asteroid and set its starting position."""
        super().__init__()
        self.ss_game = ss_game
        self.settings = ss_game.settings

        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()

        self._create_asteroid_image()
        self._position_asteroid()
        
        self.x = float(self.rect.x)

    def _create_asteroid_image(self):
        """Create a random asteroid image of a random size."""
        # Randomize image.
        images = ['asteroid_1.png', 'asteroid_2.png']
        random_image = random.choice(images)
        self.image = pygame.image.load(f'images/{random_image}')

        # Randomize size.
        random_size = random.uniform(
            self.settings.asteroid_min_size, 
            self.settings.asteroid_max_size)
        self.image = pygame.transform.smoothscale_by(self.image, random_size)

    def _position_asteroid(self):
        """Randomize asteroid starting position at the right of the screen."""
        # Position asteroid at the right of the screen.
        self.rect = self.image.get_rect() 
        self.rect.x = self.settings.screen_width

        # Randomize starting y position.
        # Keep asteroid btwn scoreboard bottom and screen bottom.
        self.rect.y = random.randint(
            self.ss_game.sb.score_rect.bottom,
            self.settings.screen_height - self.rect.height
            )

    def update(self):
        """Update asteroid position."""
        self.x -= self.settings.asteroid_speed
        self.rect.x = self.x