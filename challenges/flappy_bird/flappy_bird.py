import sys
import random

import pygame

from sound import SoundEffect
from settings import Settings
from background import Background
from game_stats import GameStats
from scoreboard import ScoreBoard
from gameover import GameOver
from bird import Bird
from pipe import Pipe

class FlappyBird:
    """Overall class to manage game assets and behavior."""
   
    def __init__(self):
        """Initialize the game, and create game resources."""
        # Initialize game utilities.
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        # Create display.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        # Set game caption and icon.
        pygame.display.set_caption('Flappy Bird')
        favicon = pygame.image.load('assets/favicon.ico')
        pygame.display.set_icon(favicon)

        # Initialize game assets.
        self.sound = SoundEffect()
        self.bird = Bird(self)
        self.background = Background(self)
        self.pipes = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.scoreboard = ScoreBoard(self)
        self.gameover = GameOver(self)

        # Declare game variables.
        self.game_active = False
        self.bird_respawn_delay = self.settings.bird_respawn_delay * 1000
        self.last_pipe_x = self.first_pipe_x = (
            (10 * self.settings.game_fps * self.settings.first_pipe_delay)
            + (self.settings.screen_width - self.settings.pipe_gap))

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active and self.bird.is_alive:
                self._update_pipes()
            if self.bird.is_alive:
                self.bird.flap_wings()
                self.background.scroll()
            if self.game_active:
                self.bird.update()

            self.bird.tilt()
            self._update_screen()
            self._check_collisions()
            self.clock.tick(self.settings.game_fps)

    def _check_events(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.save_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.stats.save_high_score()
                    sys.exit()
                elif event.key == pygame.K_SPACE and self.bird.is_alive:
                    self.bird.jump()
                    self.sound.wing_sound.play()
                    self.game_active = True
                elif event.key == pygame.K_SPACE and not self.game_active:
                    self._restart_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Respond to clicking the play button."""
        play_button_clicked = (
            self.gameover.play_btn_rect.collidepoint(mouse_pos))
        if not self.bird.is_alive and play_button_clicked:
            self._restart_game()
        
    def _check_collisions(self):
        """Respond for the bird collisions."""
        self._check_bird_pipe_collsions()
        self._check_bird_ground_collisions()

        hit_screen_top = self.bird.rect.top <= 0
        if hit_screen_top and self.bird.is_alive:
            self.bird.is_alive = False
            self.sound.hit_sound.play()
        
        if self.bird.is_alive:
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)
    
    def _check_bird_pipe_collsions(self):
        """Respond to bird-pipe collisions."""
        # The bird dies when it hits a pipe.
        hit_pipe = pygame.sprite.spritecollideany(self.bird, self.pipes)
        if hit_pipe and self.bird.is_alive:
            if pygame.sprite.spritecollideany(
                self.bird, self.pipes, pygame.sprite.collide_mask):
                self.bird.is_alive = False
                self.sound.hit_sound.play()
                self.sound.die_sound.play()

    def _check_bird_ground_collisions(self):
        """Respond to bird-ground collisions."""
        hit_ground = self.bird.rect.bottom >= self.background.base_rect.top
        ground_bird_offset = (
            self.bird.rect.x, self.background.base_rect.y - self.bird.rect.y)
        # If not already dead, play the hit sound when the bird hits the ground.
        if hit_ground and self.bird.is_alive:
            if self.background.ground_mask.overlap(self.bird.mask, ground_bird_offset):
                self.sound.hit_sound.play()
                self.bird.is_alive = False
        # The game ends only after the bird drops to the ground.
        if hit_ground and self.game_active:
            if self.background.ground_mask.overlap(self.bird.mask, ground_bird_offset):
                self.game_active = False
                self.bird.rect.bottom = self.background.base_rect.top + 5
    
    def _restart_game(self):
        """Restart the game after it ends."""
        self.bird.reset()
        self.background.choose_images()
        self.stats.reset_score() # Reset score.
        self.scoreboard.prep_current_score()
        self.pipes.empty() # Delete on-screen pipe objects.
        self.last_pipe_x = self.first_pipe_x = (
            (10 * self.settings.game_fps * self.settings.first_pipe_delay)
            + (self.settings.screen_width - self.settings.pipe_gap)) # Prep new pipes.
 
    def _update_pipes(self):
        """Create pipes and update their positions."""
        # Spawn pipes at constant horizontal distance.
        last_pipe_dx = self.settings.screen_width - self.last_pipe_x
        if last_pipe_dx >= self.settings.pipe_spacing:
            self._create_pipes()

        self.pipes.update()
        self._check_pipe_passed()

        # Track position of the last spawned pipes.
        if self.pipes:
            self.last_pipe_x = max(pipe.rect.x for pipe in self.pipes)
        else:
            self.last_pipe_x -= 10

        # Delete off-screen pipes.
        for pipe in self.pipes:
            if pipe.rect.right < 0:
                self.pipes.remove(pipe)

    def _check_pipe_passed(self):
        """Award points if the bird has crossed a pipe."""
        for pipe in self.pipes:
            bird_crossed_pipe = self.bird.rect.right >= pipe.rect.centerx
            if bird_crossed_pipe and not pipe.point_awarded:
                self.stats.update()
                pipe.point_awarded = True
        self.scoreboard.prep_current_score()

    def _create_pipes(self):
        """Create pipe pairs."""
        # Create and position top pipe.
        top_pipe = Pipe(self)
        top_pipe_max_height = 432
        top_pipe_min_height = (self.background.base_rect.top
             - (top_pipe_max_height + self.settings.pipe_gap))
        top_pipe.rect.bottom = random.uniform(
            top_pipe_max_height, top_pipe_min_height)

        # Create and position bottom pipe.
        bottom_pipe = Pipe(self)
        bottom_pipe.rect.top = (top_pipe.rect.bottom + self.settings.pipe_gap)
        
        # Add top and bottom pipe to pipe group.
        self.pipes.add(top_pipe, bottom_pipe)

    def _update_screen(self):
        """Update the images on the screen, and flip to the new screen.""" 
        self.background.blit_bg_image() 
        self.pipes.draw(self.screen)
        self.bird.blitme()

        if self.bird.is_alive:
            self.scoreboard.show_current_score()
        else:
            self.gameover.show_popup()

        self.background.blit_base()
        pygame.display.flip()

fb = FlappyBird()
fb.run_game()