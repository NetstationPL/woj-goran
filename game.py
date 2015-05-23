import pygame
from pygame.locals import *  # noqa

import pymunk
import pymunk.pygame_util

from player import Player

screen_size = (1280, 720)

def create_line(space):
    body = pymunk.Body()
    body.position = (0, screen_size[1])
    line_shape = pymunk.Segment(body, (0, -0), (screen_size[0], 0), 128)
    line_shape.elasticity = 0.5
    line_shape.collision_type = 2
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

        def standing(*largs):
            self.player.on_ground = True
            self.player.stand()
            return True

        def flying(*largs):
            self.player.on_ground = False
            return True

        self.space.add_collision_handler(1, 2, begin=standing, separate=flying)
        
        self.clock = pygame.time.Clock()
        
        self.floor = create_line(self.space)

    def initial_background(self):
        background = pygame.Surface(self.surface.get_size())
        background = background.convert()
        background.fill((128, 128, 250))
        self.surface.blit(background, (0, 0))
        image = pygame.image.load('images/land.png').convert()

        for i in range(0, screen_size[0], image.get_width()):
            self.surface.blit(image, (i, screen_size[1] - image.get_height()))


    def main(self):
        while self.gamestate == 1:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.gamestate = 0
            
            self.player.walk(0)

            keys = pygame.key.get_pressed()

            if keys[K_LEFT]:
                self.player.walk(-1)
            if keys[K_RIGHT]:
                self.player.walk()
            if keys[K_UP]:
                self.player.jump()

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
