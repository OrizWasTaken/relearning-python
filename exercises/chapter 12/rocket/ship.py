import pygame
import os

from settings import Settings

os.chdir('c:/users/oriz/desktop/relearning python/exercises/chapter 12/rocket/')

class Ship:

    def __init__(self, rg):
        """Initialize the ship and set its starting position."""
        self.settings = Settings()

        self.screen = rg.screen
        self.screen_rect = self.screen.get_rect()

        self.img = pygame.image.load('images/rocket_ship.png')
        self.img = pygame.transform.smoothscale(self.img, (self.settings.ship_width, self.settings.ship_height)) 

        self.rect = self.img.get_rect()
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.is_moving_up = False
        self.is_moving_right = False
        self.is_moving_down = False
        self.is_moving_left = False

    def update(self):
        """Update ship position"""
        if self.is_moving_up == True and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.is_moving_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.is_moving_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.is_moving_left== True and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        """Draw the ship at its current location."""  
        self.screen.blit(self.img, self.rect)