import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from typing import Tuple

class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)


class Game:
    def __init__(self, name: str, size: Tuple[int, int], fps: int = 60):
        self.name = name
        self.width, self.height = self.size = size
        self.fps = fps

    def start(self):
        ''' Runs once before game starts. Implement setup logic here.
        '''
        # Drop player in middle of screen
        self.player_pos = [self.width // 2, self.height // 2]
        self.player_speed = 4

    def on_event(self, event):
        ''' Runs once per event. Implement event handling here.
        '''
        pass

    def update(self, keys):
        ''' Runs once every frame. Implement game logic here.
        '''
        # Player movement
        if keys[pygame.K_w]:
            self.player_pos[1] -= self.player_speed
        if keys[pygame.K_s]:
            self.player_pos[1] += self.player_speed
        if keys[pygame.K_a]:
            self.player_pos[0] -= self.player_speed
        if keys[pygame.K_d]:
            self.player_pos[0] += self.player_speed

    def render(self, screen):
        ''' Runs once every frame. Implement rendering here.
        '''
        player_rect = pygame.rect.Rect(*self.player_pos, 10, 10)
        pygame.draw.rect(screen, Colors.WHITE, player_rect)

    def run(self):
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.name)
        clock = pygame.time.Clock()

        # Setup callback
        self.start()

        running = True
        while running:
            clock.tick(self.fps)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.on_event(event)

            # Game logic callback
            self.update(keys=pygame.key.get_pressed())

            # Clear canvas
            screen.fill(Colors.BLACK)
            # Render callback
            self.render(screen)
            # Update screen
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    game = Game('Boilerplate Game', (640, 480))
    game.run()
