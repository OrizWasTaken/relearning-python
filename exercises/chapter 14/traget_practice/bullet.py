import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Create a bullet object at the ship's current position."""

    def __init__(self, tp_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()

        self.settings = tp_game.settings

        self.screen = tp_game.screen
        self.ship = tp_game.ship

        # create bullet image to utilize pygame.Group.draw()
        self.image = pygame.Surface(
            (self.settings.bullet_size), 
            masks=self.settings.bullet_color,
            )
        self.rect = self.image.get_rect()
        self.rect.midleft = self.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
        