# -*- coding: utf-8 -*-
import pygame


class PlayerSprite(pygame.sprite.Sprite):

    image = None

    images = [[pygame.image.load("images/player_idle.png"), ],
              [pygame.image.load("images/player_walk1.png"),
               pygame.image.load("images/player_walk2.png"),
               pygame.image.load("images/player_walk3.png"),
               pygame.image.load("images/player_idle.png")]]
    # images_str = ["images/player_idle.png", "images/player_walk1.png",
    #               "images/player_walk2.png", "images/player_walk3.png", ]
    # default_groups = []

    # STEP = 5

    # CHANGE_ANIM_AFTER_STEPS = 5

    def get_state(self):
        return self._state

    def set_state(self, state):
        if state != self._state:
            self.frame = 0
        self._state = state

    state = property(get_state, set_state)

    def __init__(self, body):
        pygame.sprite.Sprite.__init__(self)

        self.body = body

        self.frame = 0

        self._state = 0

        self.image = self.images[0][0]

        self.rect = self.image.get_rect()
        self.rect.x = body.position[0]
        self.rect.y = body.position[1]

        # self.images = []
        # for i in self.images_str:
        #     self.images.append(pygame.image.load(i))

        # self.frames_count = 0

        # self.body = pymunk.Body(30, pymunk.moment_for_box(50, 1, 1))
        # self.body.position = (self.rect.centerx, 720 - 96)
        # self.shape = pymunk.Circle(self.body, 15, (0, 17))
        # self.shape.collision_type = 1

    def update(self):
        pygame.sprite.Sprite.update(self)

        self.frame += 1

        if self.frame == len(self.images[self.state]):
            self.frame = 0

        self.image = self.images[self.state][self.frame]

        # if state == 1:
        #     self.frames_count += 1
        #     # obsługa zmiany klatki animacji po kilku krokach
        #     if self.frames_count >= self.CHANGE_ANIM_AFTER_STEPS:
        #         if self.frame == len(self.images_str) - 1:
        #             self.frame = 0
        #         self.frame += 1
        #         self.frames_count = 0

        #     # ustawiamy kierunek poruszania się postaci
        #     if self.body.velocity[0] > 0:
        #         self.direction = 1
        #     else:
        #         self.direction = -1

        # self.image = self.images[self.frame]

        # odbicie lustrzane klatki animacji jeśli kierunek jest odpowiedni
        # if self.direction == -1:
        #     self.image = pygame.transform.flip(self.image, True, False)

        self.rect.x = self.body.position[0]
        self.rect.y = self.body.position[1]

    # def jump(self):
    #     if self.is_jumping():
    #         return
    #     self.body.apply_impulse(pymunk.vec2d.Vec2d(0, -4000))
    #     if self.is_walking():
    #         self.body.apply_impulse(
    #             pymunk.vec2d.Vec2d(5000 * self.direction * -1, 0))
