import pygame
from pygame.sprite import Sprite
from settings import Settings

class Bullet(Sprite):

    def __init__(self, ss_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        self.rect = pygame.Rect(0, 0, 
            self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = ss_game.ship.rect.midright
        
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet accross the screen."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def drawme(self):
        """Move the bullet up the screen."""
        pygame.draw.rect(self.screen, 
            self.settings.bullet_color,
            self.rect,
            )