import pygame
import sys
from settings import Settings

class BlueSkyGame:
    """Make a Pygame window with a blue background."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height
            ))
        pygame.display.set_caption('Blue Sky Game')

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
            # fill screen with sky blue
            self.screen.fill(self.settings.bg_color)

            # update the screen
            pygame.display.flip()

            # manage game fps
            self.clock.tick(60)
        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    bsg = BlueSkyGame()
    bsg.run_game()