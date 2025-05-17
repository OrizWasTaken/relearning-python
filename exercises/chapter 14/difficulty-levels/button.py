import pygame.font

class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.settings = ai_game.settings

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = self.settings.button_size
        self.button_color = self.settings.base_color
        self.msg = msg
        self.text_color = self.settings.button_text_color
        self.font = pygame.font.SysFont(None, self.settings.button_font_size)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.top -= 2.25 * self.rect.height

        # The button message needs to be prepped only once.
        self._prep_msg()

    def _prep_msg(self):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(self.msg, True, self.text_color,
        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.update_msg_position()

    def update_msg_position(self):
        """If the button has been moved, the text needs to be moved as well."""
        self.msg_image_rect.center = self.rect.center

    def set_highlighted_color(self):
        """Set the button to the highlighted color."""
        self.button_color = self.settings.highlighted_color
        self._prep_msg()

    def set_base_color(self):
        """Set the button to the base color."""
        self.button_color = self.settings.base_color
        self._prep_msg()

    def draw_button(self):
        """Draw blank button and then draw message."""
        pygame.draw.rect(self.screen, self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)