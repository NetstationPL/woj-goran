import pygame
from pygame.locals import *  # noqa

screen_size = (1024, 798)


class Game(object):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.surface = pygame.display.set_mode(screen_size, pygame.HWSURFACE)
        self.gamestate = 1
        self.initial_background()

    def initial_background(self):
        background = pygame.Surface(self.surface.get_size())
        background = background.convert()
        background.fill((128, 128, 250))
        self.surface.blit(background, (0, 0))
        image = pygame.image.load('images/2.png').convert()

        for i in range(0, 1024, 128):
            self.surface.blit(image, (i, 798 - 128))

        pygame.display.flip()

    def main(self):
        while self.gamestate == 1:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.gamestate = 0


if __name__ == "__main__":
    Game().main()
