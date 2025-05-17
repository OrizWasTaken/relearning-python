import sys

import pygame

from ship import Ship
from bullet import Bullet
from target import Target
from button import Button
from settings import Settings
from game_stats import GameStats

class TargetPractice:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.settings = Settings()
        self.stats = GameStats()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Target Practice")

        self.ship = Ship(self)
        self.target = Target(self)
        self.bullets = pygame.sprite.Group()

        self.game_active = False
        self.play_button = Button(self, 'Play')

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_target()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button()

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self):
        """Start a new game when the player clicks Play."""
        mouse_pos = pygame.mouse.get_pos()
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if not self.game_active and button_clicked:
            self._start_game()

    def _start_game(self):
        "Start a new game"
        self.game_active = True
        self.settings.init_dynamic_settings()
        self.ship.center_ship()
        self.target.center_target()
        self.bullets.empty()
        self.stats.reset_stats()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        for bullet in self.bullets:
            if bullet.rect.colliderect(self.target.rect):
                self.bullets.remove(bullet)
            elif bullet.rect.left >= self.settings.screen_width:
                self._miss_target()
                self.bullets.remove(bullet)

    def _miss_target(self):
        """Respond to the bullet missin the target."""
        if self.stats.misses_left > 1:
            self.stats.misses_left -= 1
        else:
            self.game_active = False

    def _update_target(self):
        """Check if the target is at an edge, then update positions."""
        if self.target.check_edge():
            self.settings.target_direction *= -1
        self.settings.increase_speed()
        self.target.update()
        
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill((255, 255, 255))
        self.ship.blitme()
        self.target.drawme()
        self.bullets.draw(self.screen)

        if not self.game_active:
            self.play_button.drawme()

        pygame.display.flip()

if __name__ == '__main__':
    tp = TargetPractice()
    tp.run_game()