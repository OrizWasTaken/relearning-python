import pygame
import os
from pygame.sprite import Sprite
from settings import Settings

os.chdir('C:/Users/Oriz/Desktop/relearning python/exercises/chapter 13/stars')

class Star(Sprite):
    """A class to represent a single star in the constellation"""

    def __init__(self):
        """Initialize the star"""
        super().__init__()
        self.settings = Settings()

        self.image = pygame.image.load('images/star.png')
        self.image = pygame.transform.smoothscale(self.image, self.settings.star_size)
        self.rect = self.image.get_rect()