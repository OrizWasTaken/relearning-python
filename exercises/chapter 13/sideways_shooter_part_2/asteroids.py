import pygame
import random
from pygame.sprite import Sprite
from settings import Settings

class Asteroids(Sprite):
    """A class to represent a single asteroid"""

    def __init__(self, ss_game2):
        """Initialize the asteroid and set its starting position."""
        super().__init__()
        self.settings = ss_game2.settings

        self.screen = ss_game2.screen
        self.screen_rect = self.screen.get_rect()

        images = ['asteroid_1.png', 'asteroid_2.png']
        random_image = random.choice(images)
        self.image = pygame.image.load(f'images/{random_image}')
        random_size = random.uniform(
            self.settings.asteroid_min_size, 
            self.settings.asteroid_max_size)
        self.image = pygame.transform.smoothscale_by(self.image, random_size)

        self.rect = self.image.get_rect()
        
        self.rect.x = self.settings.screen_width
        self.x = float(self.rect.x)

    def update(self):
        """Update asteroid position"""
        self.x -= self.settings.asteroid_speed
        self.rect.x = self.x