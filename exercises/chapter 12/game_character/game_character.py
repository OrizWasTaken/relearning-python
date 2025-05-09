import pygame
import sys

from bird import Bird
from settings import Settings

class FlappyBird:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # create game functionalities
        self.setting = Settings()
        self.clock = pygame.time.Clock()

        # create game window
        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height)
            )
        pygame.display.set_caption('Flappy Bird')

        # create game assets
        self.bird = Bird(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_event()
            self._update_screen()
            self.clock.tick(60) # fps = 60
    
    def _check_event(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.setting.bg_color)
        self.bird.bitme()
        pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance, and run the game.
    fb = FlappyBird()
    fb.run_game()