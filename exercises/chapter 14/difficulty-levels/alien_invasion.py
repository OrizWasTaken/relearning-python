import pygame
import sys
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from game_stats import GameStats

class AlienInvasion:
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
            (self.settings.screen_width, self.settings.screen_height,))
        pygame.display.set_caption("Alien Invasion")

        #create game assets
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Alien Invasion in an active state.
        self.game_active = False

        # Make the Play button.
        self.play_button = Button(self, 'Play')

        # Make difficulty level buttons.
        self._make_difficulty_buttons()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        new_alien_x, new_alien_y = alien_width, alien_height
        while new_alien_y <= (self.settings.screen_height - 3 * alien_height):
            while new_alien_x <= (self.settings.screen_width - 2 * alien_width):
                self._create_alien(new_alien_x, new_alien_y)
                new_alien_x += 2 * alien_width

            # Finished a row; reset x value, and increment y value.
            new_alien_x = alien_width
            new_alien_y += 2 * alien_height

    def _make_difficulty_buttons(self):
        """Make buttons that allow player to select difficulty level."""
        self.easy_button = Button(self, 'Easy')
        self.medium_button = Button(self, 'Medium')
        self.hard_button = Button(self, 'Hard')

        self.easy_button.rect.top = (
            self.play_button.rect.top + 1.5*self.play_button.rect.height)
        self.easy_button.update_msg_position()

        self.medium_button.rect.top = (
            self.easy_button.rect.top + 1.5*self.easy_button.rect.height)
        self.medium_button.update_msg_position()

        self.hard_button.rect.top = (
            self.medium_button.rect.top + 1.5*self.medium_button.rect.height)
        self.hard_button.update_msg_position()

        # create tuple of buttons for iteration
        self.difficulty_buttons = (
            self.easy_button,
            self.medium_button,
            self.hard_button,
        )

        self.medium_button.set_highlighted_color()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()
            self.clock.tick(60) # set fps to 60

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
                self._check_difficulty_buttons(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_ESCAPE: # Esc to quit came
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_SPACE:
            self.ship.is_shooting = False

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.game_active = True

            # Reset the game stats
            self.stats.reset_stats()

            # Reset the game settings.
            self.settings.initialize_dynamic_settings()

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_difficulty_buttons(self, mouse_pos):
        """Set the appropriate difficulty level."""
        easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_button_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        hard_button_clicked = self.hard_button.rect.collidepoint(mouse_pos)

        if easy_button_clicked and not self.game_active:
            self.settings.difficulty_level = 'easy'
            self._highlight_button(self.easy_button)
        elif medium_button_clicked and not self.game_active:
            self.settings.difficulty_level = 'medium'
            self._highlight_button(self.medium_button)
        elif hard_button_clicked and not self.game_active:
            self.settings.difficulty_level = 'hard'
            self._highlight_button(self.hard_button)
    
    def _highlight_button(self, difficulty_button):
        """"""
        for button in self.difficulty_buttons:
            button.set_base_color()
        difficulty_button.set_highlighted_color()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update() # call self.update() on each bullet

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
        
        # Check if every alien has been destroyed
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
         
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
            self._ship_hit()

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

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()
            
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _check_game_end(self):
        if self.ships_used == self.settings.ship_limit:
            self.stats.reset_stats()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
            for button in self.difficulty_buttons:
                button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()