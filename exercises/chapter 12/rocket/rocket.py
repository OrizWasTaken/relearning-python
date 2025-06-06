import pygame
import sys

from settings import Settings
from ship import Ship

class Rocket:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height),
            )
        pygame.display.set_caption("Rocket")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.ship.is_moving_up = True
        elif event.key == pygame.K_RIGHT:
            self.ship.is_moving_right = True
        elif event.key == pygame.K_DOWN:
            self.ship.is_moving_down = True
        elif event.key == pygame.K_LEFT:
            self.ship.is_moving_left = True

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.is_moving_up = False
        elif event.key == pygame.K_RIGHT:
            self.ship.is_moving_right = False
        elif event.key == pygame.K_DOWN:
            self.ship.is_moving_down = False
        elif event.key == pygame.K_LEFT:
            self.ship.is_moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()



if __name__ == '__main__':
    rg = Rocket()
    rg.run_game()
