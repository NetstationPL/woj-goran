import pygame
from pygame.locals import *  # noqa

import pymunk
import pymunk.pygame_util

from player import Player

screen_size = (1024, 798)

def create_line(space):
    body = pymunk.Body()
    body.position = (0, 798)
    line_shape = pymunk.Segment(body, (0, -0), (1024, 0), 128)
    line_shape.elasticity = 0.5
    space.add(line_shape)
    return line_shape

class Game(object):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.space = pymunk.Space()
        self.space.gravity = (0, 100)

        self.surface = pygame.display.set_mode(screen_size, pygame.HWSURFACE)
        self.gamestate = 1
        self.initial_background()
        self.players = pygame.sprite.RenderUpdates()
        self.player = Player()
        self.player.rect.bottom = screen_size[1] - 128 + 20
        self.players.add(self.player)
        self.space.add(self.player.body, self.player.shape)
        self.clock = pygame.time.Clock()
        self.STEP = 5
        self.floor = create_line(self.space)

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

            #self.player.body.velocity = pymunk.vec2d.Vec2d(0, 0)
            if keys[K_LEFT]:
                self.player.walk = self.STEP * -1
            if keys[K_RIGHT]:
                self.player.walk = self.STEP
            if keys[K_UP]:
                self.player.body.velocity = pymunk.vec2d.Vec2d(0, -100)

            self.players.update()
            self.initial_background()
            self.players.draw(self.surface)
            
            #pymunk.pygame_util.flip_y = False            
            #pymunk.pygame_util.draw(self.surface, self.space)
                
            pygame.display.flip()
            self.clock.tick(60)
            self.space.step(1/60.0)

if __name__ == "__main__":
    Game().main()
