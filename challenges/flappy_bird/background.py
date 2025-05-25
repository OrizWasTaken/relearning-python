import pygame
import random

class Background:
    """A class to represent the game's background."""

    def __init__(self, fb_game):
        """Initialize the background properties."""
        self.settings = fb_game.settings
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()

        # Select the background, pipe, and base images.
        self.bg_images = [
            'background1.bmp', 'background2.bmp',
            'background3.bmp','background4.bmp',
            'background5.bmp','background6.bmp',
            'background7.bmp','background8.bmp']
        self.pipe_images = [
            'bluepipe.bmp', 'brownpipe.bmp', 'goldpipe.bmp', 'greenpipe.bmp',
            'greypipe.bmp', 'orangepipe.bmp', 'purplepipe.bmp', 'redpipe.bmp']
        self.base_images = ['base1.bmp', 'base2.bmp']

        self.choose_images()

        # Position the base at the bottom of the screen.
        self.base_rect = self.base_image.get_rect()
        self.base_rect.bottom = self.screen_rect.bottom

        # A mask object for the entire ground.
        ground_image = pygame.Surface(
            (self.screen_rect.width, self.base_rect.height))
        self.ground_mask = pygame.mask.from_surface(ground_image)

        # Precise x position of the first base tile.
        self.bx = float(self.base_rect.x)

    def choose_images(self):
        """
        Randomly choose the background, base and pipe images.
        """
        self.bg_image = pygame.image.load(f'assets/backgrounds/{random.choice(self.bg_images)}')
        self.base_image = pygame.image.load(f'assets/bases/{random.choice(self.base_images)}')
        self.pipe_image = pygame.image.load(f'assets/pipes/{random.choice(self.pipe_images)}')

    def scroll(self):
        """Update background positon to create scrolling effect."""
        # Update x-position of first base tile by game speed.          
        self.bx -= self.settings.game_speed
        self.base_rect.x = self.bx

        # Reset x-position of first base tile when offscreen.
        if self.base_rect.right <= 0:
            self.bx = 0

    def blit_bg_image(self):
        """Fill the screen with the background image."""    
        self.screen.blit(self.bg_image, (0,0))

    def blit_base(self):
        """Tile the bottom of the screen with the base image."""
        for x in range(self.base_rect.left, self.screen_rect.width, self.base_rect.width):
            self.screen.blit(self.base_image, (x, self.base_rect.top))