import pygame
import itertools
import random

class Bird:
    """"A class to manage the bird."""

    def __init__(self, fb_game):
        """Initialize the bird and set its starting properties."""
        self.settings = fb_game.settings

        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()

        self._choose_skin()
        self.reset()

        self.a = self.settings.bird_acceleration
        self.last_frame_update = pygame.time.get_ticks()

    def _choose_skin(self):
        """Randomly select a bird skin and load its animation frames."""
        skin = random.choice(['red', 'blue', 'yellow'])
        paths = {
            'upflap': f'assets/birds/{skin}bird-upflap.bmp',
            'midflap': f'assets/birds/{skin}bird-midflap.bmp',
            'downflap': f'assets/birds/{skin}bird-downflap.bmp'}
        self.images = {
            flap : pygame.image.load(file) for flap, file in paths.items()
        }
        # Iterator for animation.
        self.images_cycler = itertools.cycle(self.images.values())

    def reset(self):
        """Reset all bird properties."""
        # Bring the bird to life.
        self.is_alive = True

        self.image = self.images['midflap']

        # Position the bird near the center of the screen.
        self.rect = self.image.get_rect(
            centerx=0.25 * self.screen_rect.width,
            centery=self.screen_rect.centery)
        self.y = float(self.rect.y)

        # Zero the bird's tilt angle and vertical velocity.
        self.tilt_angle = 0
        self.v = 0

    def update(self):
        """Update the vertical position of the bird."""
        self.v += self.a
        self.y += self.v
        self.rect.y = self.y

    def flap_wings(self):
        """Advance to the next animation frame."""
        time_elapsed = (pygame.time.get_ticks() - self.last_frame_update)
        if time_elapsed >= self.settings.bird_animation_delay * 1000:
            self.image = next(self.images_cycler)
            self.last_frame_update += time_elapsed

    def jump(self): 
        """Make the bird jump."""
        self.v = -1 * self.settings.jump_force

    def tilt(self):
        """Tilt the bird."""
        if self.v < 0:
            self.tilt_angle = max(-25, self.tilt_angle - 5)
        elif self.v > 5:
            self.tilt_angle = min(90, self.tilt_angle + 4)
        elif self.v > 0:
            self.tilt_angle = min(90, self.tilt_angle + 1)

        self.rotated_image = self.image
        if self.tilt_angle:
            self.rotated_image = pygame.transform.rotozoom(self.image, -self.tilt_angle, 1)
            self.rect = self.rotated_image.get_rect(center=self.rect.center)
            self.mask = pygame.mask.from_surface(self.rotated_image)

    def blitme(self):
        """Draw the bird at its current location."""
        self.screen.blit(self.rotated_image, self.rect)