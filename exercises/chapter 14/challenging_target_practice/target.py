import pygame

class Target:
    """A class to represent the target"""

    def __init__(self, tp_game):
        """Initialize the target and set its starting position."""
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect((0,0), (self.settings.target_size))

        self.center_target()

    def update(self):
        """Update target position."""
        self.y += self.settings.target_speed * self.settings.target_direction
        self.rect.y = self.y

    def drawme(self):
        """Draw the target at its current location."""
        pygame.draw.rect(self.screen, self.settings.target_color, self.rect)

    def check_edge(self):
        """Return True if target is at edge of screen."""
        return (self.rect.bottom >= self.screen_rect.bottom) or (self.rect.top <= 0)
    
    def center_target(self):
        """Center the target on the screen."""
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)
