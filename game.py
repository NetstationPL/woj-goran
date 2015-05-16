import pygame
from pygame.locals import *  # noqa

from player import Player

screen_size = (1024, 798)


class Game(object):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.surface = pygame.display.set_mode(screen_size, pygame.HWSURFACE)
        self.gamestate = 1
        self.initial_background()
        self.players = pygame.sprite.RenderUpdates()
        self.player = Player()
        self.player.rect.bottom = screen_size[1] - 128 + 20
        self.players.add(self.player)
        self.clock = pygame.time.Clock()
        self.STEP = 5

    def initial_background(self):
        background = pygame.Surface(self.surface.get_size())
        background = background.convert()
        background.fill((128, 128, 250))
        self.surface.blit(background, (0, 0))
        image = pygame.image.load('images/2.png').convert()

        for i in range(0, 1024, 128):
            self.surface.blit(image, (i, 798 - 128))


    def main(self):
        while self.gamestate == 1:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.gamestate = 0
            self.player.walk = 0
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                self.player.walk = self.STEP * -1
            if keys[K_RIGHT]:
                self.player.walk = self.STEP


            self.players.update()
            self.initial_background()
            self.players.draw(self.surface)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().main()
