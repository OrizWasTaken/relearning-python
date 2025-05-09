class Settings:
    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # ship settings
        self.ship_height = 80
        self.ship_width = 80
        self.ship_speed = 5

        # bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (0,0,0)
        self.bullet_limit = 5