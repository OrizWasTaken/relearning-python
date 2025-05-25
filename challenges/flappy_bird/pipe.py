from pygame.sprite import Sprite
import pygame.mask

class Pipe(Sprite):
    "A class to represent a single pipe."""

    def __init__(self, fb_game):
        """Initialize the pipe and set its attributes."""
        super().__init__()
        self.settings = fb_game.settings
        self.background = fb_game.background

        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = self.background.pipe_image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # Create the pipe off-screen.
        self.rect.left = self.screen_rect.right

        # Precise x-position of the pipe.
        self.x = float(self.rect.x)
        
        # Track if a point has been awarded for passing the pipe.
        self.point_awarded = False

    def update(self):
        """Update the x-position of the pipe to create a scrolling effect."""
        self.x -= self.settings.game_speed
        self.rect.x = self.x