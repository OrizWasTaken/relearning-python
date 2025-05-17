import pygame.font

class Button:
    """A class to represent a button"""

    def __init__(self, ai_game, msg):
        """Initialize the button and it's starting postion."""
        self.settings = ai_game.settings

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.msg = msg
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect((0,0), (self.width, self.height))
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw button to screen"""
        pygame.draw.rect(self.screen, self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)