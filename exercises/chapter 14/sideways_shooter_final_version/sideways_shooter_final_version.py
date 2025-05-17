import pygame
import sys
from random import randint
from time import sleep
from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
from bullet import Bullet
from asteroids import Asteroids
from scoreboard import ScoreBoard

class SidewaysShooter2:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # create game utilities
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.stats = GameStats(self)

        # create game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption("Sideways Shooter")

        # create game assets
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.play_button = Button(self, 'Play')
        self.sb = ScoreBoard(self)

        # set game variables
        self.game_active = False
        self.last_spawn_time = pygame.time.get_ticks()
        self.last_speedup_time = pygame.time.get_ticks()
        print(self.last_speedup_time)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_asteroids()
                self._speedup_game()

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
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up =  True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down =  False

    def _check_play_button(self, mouse_pos):
        """Respond to play button being clicked"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        
        if button_clicked and not self.game_active:
            self.game_active = True
            self.stats.reset_stats()
            self.settings.initialize_dynamic_settings()

            self.asteroids.empty()
            self.ship.center_ship()

            self.sb.prep_score()
            self.sb.prep_ships()

            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        for bullet in self.bullets.copy():
            if bullet.rect.x >= self.settings.screen_width:
                self.bullets.remove(bullet)
        self.bullets.update()

        # Look for bullet-asteroid collisions.
        self._check_bullet_asteroid_collisions()

    def _update_asteroids(self):
        """Create asteroids, update their position and get rid of old ones."""
        self._create_asteroid()
        self.asteroids.update()

        # Get rid of asteroids that have disappeared.
        for asteroid in self.asteroids.copy():
            if asteroid.rect.right <= 0:
                self.asteroids.remove(asteroid)

        self._check_asteroid_ship_collisions()
        self._check_asteroids_left()

    def _create_asteroid(self):
        """Create and add asteroid to the group of asteroids."""
        # Delay asteroid spawning.
        elasped_time = pygame.time.get_ticks() - self.last_spawn_time
        if elasped_time >= self.settings.asteroid_spawn_interval * 1000:
            new_asteroid = Asteroids(self)
            self.asteroids.add(new_asteroid)
            self.last_spawn_time += elasped_time

    def _check_bullet_asteroid_collisions(self):
        """Respond to bullet-asteroid collisions."""
        # Remove any bullets and asteroids that have collided.
        collisions = pygame.sprite.groupcollide(
        self.bullets, self.asteroids, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.asteroid_points * len(aliens)
            self.sb.check_high_score()
            self.sb.prep_score()
            self.sb.prep_high_score()

    def _check_asteroid_ship_collisions(self):
        """Respond to asteroid-ship collisions."""
        if pygame.sprite.spritecollideany(self.ship, self.asteroids):
            self._reset_game()
            
    def _check_asteroids_left(self):
        """Check if any asteroid has reached the left of the screen."""
        for asteroid in self.asteroids.sprites():
            if asteroid.rect.left <= 0:
                self._reset_game()
                break

    def _reset_game(self):
        """Reset game assets"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.bullets.empty()
            self.asteroids.empty()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False 
            pygame.mouse.set_visible(True)

    def _speedup_game(self):
        """Increase game speed"""
        elapsed_time = pygame.time.get_ticks() - self.last_speedup_time
        if elapsed_time >= self.settings.speedup_interval * 1000:
            self.settings.increase_speed()
            self.last_speedup_time += elapsed_time

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.asteroids.draw(self.screen)
        for bullet in self.bullets:
            bullet.drawme()
        self.sb.show_score()

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == "__main__":
    ss_game2 = SidewaysShooter2()
    ss_game2.run_game()