import pygame
import sys
from settings import Settings
from star import Star

class StarsGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()

        self._create_constellation()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_event()
            self._update_screen()
            self.clock.tick(60)

    def _check_event(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_constellation(self):
        """Create the constellation of stars."""
        star_width, star_height = self.settings.star_size

        new_star_x, new_star_y = star_width, star_height
        while new_star_y <= (self.settings.screen_height - 2 * star_height):
            while new_star_x <= (self.settings.screen_width - 2 * star_width):
                self._create_star(new_star_x, new_star_y)
                new_star_x += 2 * star_width
            
            new_star_x = star_width
            new_star_y += 2 * star_height
    
    def _create_star(self, x_position, y_position):
        """Create an star and place it in the constellation."""
        new_star = Star(self)
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    stars = StarsGame()
    stars.run_game()