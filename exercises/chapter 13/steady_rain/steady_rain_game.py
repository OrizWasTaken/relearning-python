import pygame
import sys
from settings import Settings
from raindrop import Raindrop

class SteadyRainGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Raindrops")

        self.raindrops = pygame.sprite.Group()

        self._create_rain()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_event()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(60)

    def _check_event(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_rain(self):
        """Create the constellation of stars."""
        raindrop = Raindrop(self)
        raindrop_width, self.raindrop_height = raindrop.rect.size

        new_raindrop_x, new_raindrop_y = raindrop_width, self.raindrop_height
        while new_raindrop_y <= (self.settings.screen_height - 4 * self.raindrop_height):
            while new_raindrop_x <= (self.settings.screen_width - 2 * raindrop_width):
                self._create_raindrop(new_raindrop_x, new_raindrop_y)
                new_raindrop_x += 5 * raindrop_width
            
            new_raindrop_x = raindrop_width
            new_raindrop_y += 5 * self.raindrop_height
    
    def _create_raindrop(self, x_position, y_position):
        """Create an star and place it in the constellation."""
        new_raindrop = Raindrop(self)
        new_raindrop.rect.x = x_position
        new_raindrop.y = y_position
        self.raindrops.add(new_raindrop)

    def _update_raindrops(self):
        """Update position of bullets and get renew fallen raindrops."""
        for raindrop in self.raindrops.copy():
            if raindrop.rect.top > self.settings.screen_height:
                raindrop.y = self.raindrop_height

        self.raindrops.update()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    steady_rain = SteadyRainGame()
    steady_rain.run_game()