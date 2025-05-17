import pygame
from pygame.sprite import Sprite
from settings import Settings

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ss_game, scoreboard=False):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.ss_game = ss_game
        self.settings = ss_game.settings

        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()

        self._create_image(scoreboard)

        self.rect = self.image.get_rect()

        self.center_ship()

        self.moving_up =  False
        self.moving_down =  False
    
    def _create_image(self, scoreboard):
        """Create ship image based on it's function"""
        self.img = pygame.image.load('images/rocket_ship.png')
        if not scoreboard:
            self.img = pygame.transform.smoothscale_by(self.img, 0.075)
            self.image = pygame.transform.rotate(self.img, -90)
        else:
            self.image = pygame.transform.smoothscale_by(self.img, 0.05)

    def update(self):
        """Update ship position"""
        if self.moving_up and self.rect.top > self.ss_game.sb.score_rect.bottom:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def center_ship(self):
        """Position ship at midleft of screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        
    def blitme(self):
        """Draw the ship at its current location.""" 
        self.screen.blit(self.image, self.rect)