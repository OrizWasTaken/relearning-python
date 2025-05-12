import pygame
import os
from pygame.sprite import Sprite
from settings import Settings

os.chdir('C:/Users/Oriz/Desktop/relearning python/exercises/chapter 13/raindrops')

class Raindrop(Sprite):
    """A class to represent a single raindrop"""

    def __init__(self, rd_game):
        """Initialize the raindrop"""
        super().__init__()
        self.settings = Settings()

        self.image = pygame.image.load('images/raindrop.png')
        self.image = pygame.transform.smoothscale(self.image, self.settings.raindrop_size)
        self.rect = self.image.get_rect()

        self.y = float(self.rect.y)

    def update(self):
        """Update raindrop position"""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y