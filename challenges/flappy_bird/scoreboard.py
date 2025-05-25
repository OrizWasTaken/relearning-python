import pygame

class ScoreBoard:
    """A class to represent the game's scoreboard."""

    def __init__(self, fb_game):
        """Initialize the scoreboard."""
        self.settings = fb_game.settings
        self.stats = fb_game.stats

        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()

        self._load_images()

        self.scoreboard_rect = self.scoreboard_image.get_rect()
        self.scoreboard_rect.center = self.screen_rect.center

        self.new_tag_rect = self.scoreboard_image.get_rect()
        self.new_tag_rect.topleft = (
            self.scoreboard_rect.left+203, self.scoreboard_rect.top+87)
        
        self.medal_rects = {
           medal: image.get_rect(
               topleft=(self.scoreboard_rect.left+40, self.scoreboard_rect.top+65)) 
            for medal, image in self.medal_images.items()}

        self.big_digit_height = self.big_digit_images['1'].get_height()
        self.small_digit_height = self.small_digit_images['1'].get_height()

        self.prep_current_score()

    def _load_images(self):
        """Load the images for the scoreboard and its contents."""
        self.scoreboard_image = pygame.image.load('assets/gameover/scoreboard.bmp')
        self.new_tag_image = pygame.image.load('assets/gameover/new.bmp')
        self.big_digit_images = {
            str(i): pygame.image.load(f'assets/numbers/big_{i}.bmp') for i in range(10)}
        self.small_digit_images = {
            str(i): pygame.image.load(f'assets/numbers/small_{i}.bmp') for i in range(10)}

        medals = ['bronze', 'silver', 'gold', 'platinum']
        self.medal_images = {
            medal: pygame.image.load(f'assets/medals/{medal}.bmp') for medal in medals}
        
    def prep_current_score(self):
        """Prep the score image at the top of the screen."""
        self.score = int(self.stats.score)
        self.cs_score_images = [
            self.big_digit_images[num] for num in str(self.score)]
        
        # A rect for the current score.
        rect_width = sum([image.get_width() for image in self.cs_score_images])
        self.cs_rect = pygame.Rect(
            self.screen_rect.center, (self.big_digit_height, rect_width))
        self.cs_rect.top = 75

    def _prep_final_score(self):
        """Prep the score image for the game over scoreboard."""
        self.fs_score_images = [
            self.small_digit_images[num] for num in str(self.score)]
        
        # A rect for the final score.
        rect_width = sum([image.get_width() for image in self.fs_score_images])
        self.fs_rect = pygame.Rect((0,0), (rect_width, self.small_digit_height))
        self.fs_rect.topright = (self.scoreboard_rect.right-33, self.scoreboard_rect.top+50)

    def _prep_high_score(self):
        """Prep the high score image for the game over scoreboard."""
        high_score = int(self.stats.high_score)
        self.hs_score_images = [
            self.small_digit_images[num] for num in str(high_score)]
        
        # A rect for the high score.
        rect_width = sum([image.get_width() for image in self.hs_score_images])
        self.hs_rect = pygame.Rect((0,0), (rect_width, self.small_digit_height))
        self.hs_rect.bottomright = (self.scoreboard_rect.right-33, self.scoreboard_rect.bottom-28)

    def _prep_medal(self):
        """Prep the medals for the game over scoreboard."""
        self.medal = None
        if self.score >= self.settings.platinum_min:
            self.medal  = 'platinum'
        elif self.score >= self.settings.gold_min:
            self.medal  = 'gold'
        elif self.score >= self.settings.silver_min:
            self.medal  = 'silver'
        elif self.score >= self.settings.bronze_min:
            self.medal  = 'bronze'

        self.medal_image = self.medal_images.get(self.medal)
        self.medal_rect = self.medal_rects.get(self.medal)

    def show_current_score(self):
        """Render the current score at the top of the screen."""
        current_x = self.cs_rect.left
        for image in self.cs_score_images:
            self.screen.blit(image, (current_x, self.cs_rect.top))
            current_x += image.get_width()

    def _show_scores(self):
        """Render the final score and high score on the scoreboard."""
        # Blit the final score.
        current_x = self.fs_rect.left
        for image in self.fs_score_images:
            self.screen.blit(image, (current_x, self.fs_rect.top))
            current_x += image.get_width()

        # Blit the high score.
        current_x = self.hs_rect.left
        for image in self.hs_score_images:
            self.screen.blit(image, (current_x, self.hs_rect.top))
            current_x += image.get_width()

    def show_scoreboard(self):
        """Display the scoreboard on the screen."""
        self._prep_final_score()
        self._prep_high_score()
        self._prep_medal()

        self.screen.blit(self.scoreboard_image, self.scoreboard_rect)
        self._show_scores()
        if self.medal_image:
            self.screen.blit(self.medal_image, self.medal_rect)      
        if self.stats.high_score_broken:
            self.screen.blit(self.new_tag_image, self.new_tag_rect)
