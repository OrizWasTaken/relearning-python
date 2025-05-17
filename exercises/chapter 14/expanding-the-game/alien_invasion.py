import pygame
import sys
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from game_stats import GameStats
from scoreboard import ScoreBoard

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # Initialize game utiliies.
        pygame.init()
        self._initialize_game_utilities()

        # Create game window.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height,))
        pygame.display.set_caption("Alien Invasion")

        # Initialize game assets.
        self._initialize_game_assets()

        # Start Alien Invasion in an active state.
        self.game_active = False

    def _initialize_game_utilities(self):
        """Initialize core game utilities."""
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.stats = GameStats(self) 

    def _initialize_game_assets(self):
        """Initialize game assets and asset groups."""
        self.ship = Ship(self)
        self.sb = ScoreBoard(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self._create_buttons()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width.
        alien_width, alien_height = Alien(self).rect.size

        new_alien_x, new_alien_y = alien_width, alien_height
        while new_alien_y <= (self.settings.screen_height - 3 * alien_height):
            while new_alien_x <= (self.settings.screen_width - 2 * alien_width):
                self._create_alien(new_alien_x, new_alien_y)
                new_alien_x += 2 * alien_width

            # Finished a row; reset x value, and increment y value.
            new_alien_x = alien_width
            new_alien_y += 2 * alien_height

    def _create_buttons(self):
        """Create all buttons for the game."""
        self.play_button = Button(self, 'Play')

        self.easy_button = Button(self, 'Easy')
        self.easy_button.rect.top = (
            self.play_button.rect.top + 1.5 * self.play_button.height)
        self.easy_button.update_msg_position()

        self.medium_button = Button(self, 'Meduim')
        self.medium_button.rect.top = (
            self.easy_button.rect.top + 1.5 * self.play_button.height)
        self.medium_button.update_msg_position()

        # Highlight meduim button to reflect initial game difficulty.
        self.medium_button.set_highlighted_color()

        self.hard_button = Button(self, 'Hard')
        self.hard_button.rect.top = (
            self.medium_button.rect.top + 1.5 * self.play_button.height)
        self.hard_button.update_msg_position()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()
            self.clock.tick(60) # set fps to 60.

    def _check_events(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.save_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_buttons()

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_ESCAPE: # Esc to quit came.
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.game_active:
            self._start_game()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_SPACE:
            self.ship.is_shooting = False

    def _check_buttons(self):
        """Check if either the play or difficulty buttons are clicked."""
        if not self.game_active:
            mouse_pos = pygame.mouse.get_pos()

            # Start a new game when the player clicks Play.
            if self.play_button.rect.collidepoint(mouse_pos):
                self._start_game()

            # Change game difficulty 
            # when the player clicks a difficulty button.
            self._check_difficulty_buttons(mouse_pos)

    def _check_difficulty_buttons(self, mouse_pos):
        """"""
        if self.easy_button.rect.collidepoint(mouse_pos):
            self.settings.difficulty_level = 'easy'
            self.highlight_button(self.easy_button)
        elif self.medium_button.rect.collidepoint(mouse_pos):
            self.settings.difficulty_level = 'medium'
            self.highlight_button(self.medium_button)
        elif self.hard_button.rect.collidepoint(mouse_pos):
            self.settings.difficulty_level = 'hard'
            self.highlight_button(self.hard_button)

    def highlight_button(self, button):
        """Highlight a button, and set other buttons to base color."""
        # set button color to base color for all buttons
        self.easy_button.set_base_color()
        self.medium_button.set_base_color()
        self.hard_button.set_base_color()

        # highlight specific button
        button.set_highlighted_color()

    def _start_game(self):
        """Start new game."""
        # Reset game settings and stats.
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.sb.prep_images()

        # Get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        self.game_active = True

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Look for bullets hitting aliens.
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
        self.bullets, self.aliens, True, True)
        
        # Check if every alien has been destroyed.
        if not self.aliens:
            self._start_new_level()

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

    def _start_new_level(self):
        """Prep and start a new level."""
        # Destroy existing bullets and create new fleet.
        self.bullets.empty()
        self._create_fleet()

        self.settings.increase_speed()

        # Increase level.
        self.stats.level += 1
        self.sb.prep_level()
         
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._check_ships_left()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()
    
    def _check_fleet_edges(self):
        """Respond appropriately if any alien has reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._check_ships_left()
                break

    def _check_ships_left(self):
        """Respond to the ship damage based on ships left."""
        if self.stats.ships_left > 0:
            sleep(0.5) # Pause.
            self._restart_level() 
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _restart_level(self):
        """Restart current level after ship damage."""
        # Decrement ships_left, and update scoreboard.
        self.stats.ships_left -= 1
        self.sb.prep_ships()

        # Get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()
        
        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()
        
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()