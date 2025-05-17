import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.settings = ai_game.settings

        # get rectangular area of screen
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rectangular area
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # set ship rect position relative to screen rect
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # ship motion
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position"""
        # Update the ship's x value, not the rect.
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left == True and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location."""  
        self.screen.blit(self.image, self.rect)