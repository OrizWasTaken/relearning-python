import pygame

class GameOver:
    """A class to represent the game over pop-up."""

    def __init__(self, fb_game):
        """Initialize the contents of the game over pop-up."""
        margin = 20 # The margin between the contents.
        self.scoreboard = fb_game.scoreboard

        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()

        # Load the 'game over' image and set its position.
        self.game_over_image = (
            pygame.image.load('assets/gameover/gameover.bmp'))
        self.game_over_rect = self.game_over_image.get_rect(
            center=self.scoreboard.scoreboard_rect.center)
        self.game_over_rect.bottom = self.scoreboard.scoreboard_rect.top - margin

        # Load the play button image and set its position.
        self.play_btn_image = (
            pygame.image.load('assets/gameover/playbutton.bmp'))
        self.play_btn_rect = self.play_btn_image.get_rect()
        self.play_btn_rect.top = self.scoreboard.scoreboard_rect.bottom + margin
        self.play_btn_rect.left = self.scoreboard.scoreboard_rect.left

        # Load the leaderboard button image and set its position.
        self.leaderboard_btn_image = (
            pygame.image.load('assets/gameover/leaderboardbutton.bmp'))
        self.leaderboard_btn_rect = self.leaderboard_btn_image.get_rect()
        self.leaderboard_btn_rect.top = self.scoreboard.scoreboard_rect.bottom + margin
        self.leaderboard_btn_rect.right = self.scoreboard.scoreboard_rect.right

    def show_popup(self):
        """Display the contents of the game over pop-up on the screen."""
        self.screen.blit(self.game_over_image, self.game_over_rect)
        self.scoreboard.show_scoreboard()
        self.screen.blit(self.play_btn_image, self.play_btn_rect)
        self.screen.blit(self.leaderboard_btn_image, self.leaderboard_btn_rect)