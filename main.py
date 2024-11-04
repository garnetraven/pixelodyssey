import pygame
import sys

from globals import *

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

        self.clock = pygame.time.Clock()

        self.running = True

    def start(self) -> None:
        self.loop()
        self.close()

    def loop(self) -> None:
        while self.running:
            self.update()
            self.draw()

    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        pygame.display.flip()
        self.clock.tick(FPS)

    def close(self) -> None:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.start()
