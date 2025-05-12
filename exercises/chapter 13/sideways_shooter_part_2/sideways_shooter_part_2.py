import pygame
import sys
from random import randint
from time import sleep
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from asteroids import Asteroids

class SidewaysShooter2:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # create game utilities
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.stats = GameStats()

        # create game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption("Sideways Shooter")

        # create game assets
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()

        # set game variables
        self.asteroid_spawn_timer = 0
        self.game_active = True

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.__check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_asteroids()
                
            self._update_screen()
            self.clock.tick(60)

    def __check_events(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
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
        # Delay asteroid spawning.
        self.asteroid_spawn_timer += 1
        if self.asteroid_spawn_timer == self.settings.asteroid_spawn_delay:
            self._create_asteriod()
            self.asteroid_spawn_timer = 0

        # Get rid of asteriods that have disappeared.
        for asteroid in self.asteroids.copy():
            if asteroid.rect.right <= 0:
                self.asteroids.remove(asteroid)

        self.asteroids.update()

        # Look for asteroid-ship collisions.
        self._check_asteroid_ship_collisions()

        # Look for asteroids hitting the left of the screen.
        self._check_asteriods_left()

    def _create_asteriod(self):
        """Create an asteroid at a random position"""
        new_asteriod = Asteroids(self)
        new_asteriod.rect.y = randint(
           0, self.settings.screen_height - new_asteriod.rect.height)
        self.asteroids.add(new_asteriod)

    def _check_bullet_asteroid_collisions(self):
        """Respond to bullet-asteroid collisions."""
        # Remove any bullets and asteroids that have collided.
        collisions = pygame.sprite.groupcollide(
        self.bullets, self.asteroids, True, True)

    def _check_asteroid_ship_collisions(self):
        """Respond to asteroid-ship collisions."""
        if pygame.sprite.spritecollideany(self.ship, self.asteroids):
            self._reset_game()
            
    def _check_asteriods_left(self):
        """Check if any asteriod has reached the left of the screen."""
        for asteriod in self.asteroids.sprites():
            if asteriod.rect.left <= 0:
                self._reset_game()
                break

    def _reset_game(self):
        """Reset game assets"""
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1
            print(self.stats.ships_left)

            # Get rid of any remaining bullets and asteroids.
            self.bullets.empty()
            self.asteroids.empty()
            
            # center the ship.
            self.ship.y = self.ship.screen_rect.centery

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
        

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.asteroids.draw(self.screen)
        for bullet in self.bullets:
            bullet.drawme()
        pygame.display.flip()

if __name__ == "__main__":
    ss_game2 = SidewaysShooter2()
    ss_game2.run_game()