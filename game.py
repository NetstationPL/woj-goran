import pygame
from pygame.locals import *  # noqa

screen_size = (1024, 798)


class Game(object):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.surface = pygame.display.set_mode(screen_size, pygame.HWSURFACE)
        self.gamestate = 1

    def main(self):
        while self.gamestate == 1:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.gamestate = 0

if __name__ == "__main__":
    Game().main()
