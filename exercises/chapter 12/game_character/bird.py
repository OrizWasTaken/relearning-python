import pygame
import os
from settings import Settings

os.chdir('c:/users/oriz/desktop/relearning python/exercises/chapter 12/game_character/')

class Bird:
    """A class to manage a FlappyBird instance"""
    def __init__(self, fb_game):
        """Initialize the bird and set its starting position."""
        # get rectangular area of screen
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()

        # load bird image and get it's rectangular area
        self.img = pygame.image.load('images/yellowbird-midflap.png')
        self.rect = self.img.get_rect()

        # set bird rect to center of screen rect
        self.rect.center = self.screen_rect.center

    def bitme(self):
        """Draw the bird at its current location."""  
        self.screen.blit(self.img, self.rect)



