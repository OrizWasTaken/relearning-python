import pygame
import os

from settings import Settings

os.chdir('C:/Users/Oriz/Desktop/relearning python/exercises/chapter 13/sideways_shooter_part_2/')

class Ship:
    """A class to manage the ship."""

    def __init__(self, ss_game):
        """Initialize the ship and set its starting position."""
        self.settings = Settings()

        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()

        self.img = pygame.image.load('images/rocket_ship.png')
        self.img = pygame.transform.smoothscale_by(self.img, 0.075)
        self.img = pygame.transform.rotate(self.img, -90)

        self.rect = self.img.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        self.moving_up =  False
        self.moving_down =  False

    def update(self):
        """Update ship position"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location.""" 
        self.screen.blit(self.img, self.rect)