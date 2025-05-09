import pygame
import sys

class Keys:

    def __init__(self):
        """Initialize pygame and create screen"""
        pygame.init()

        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption("Keys")

        self.clock = pygame.time.Clock()

    def run(self):
        """Start the main loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
                    if event.key == pygame.K_q:
                        sys.exit()

            self.clock.tick(60)

    

if __name__ == "__main__":
    keys = Keys()
    keys.run()