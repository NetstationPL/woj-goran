# -*- coding: utf-8 -*-
import pygame
import pymunk


class Player(pygame.sprite.Sprite):
    image = pygame.image.load("images/player_idle.png")
    images_str = ["images/player_idle.png", "images/player_walk1.png", "images/player_walk2.png", "images/player_walk3.png", ]
    default_groups = []
    STEP = 5
    CHANGE_ANIM_AFTER_STEPS = 5

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.default_groups)

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
  
        self.jumping = False

        self.frame = 0
        self.images = []
        for i in self.images_str:
            self.images.append(pygame.image.load(i))
        self.frames_count = 0

        self.walk_delta = 0

        self.direction = 1
        self.body = pymunk.Body(30, pymunk.moment_for_box(50, 100, 128))
        self.body.position = (self.rect.centerx, 768 - self.rect.centery)
        self.shape = pymunk.Circle(self.body, 25)
        self.shape.collision_type = 1
        self.on_ground = True

    def update(self):
        pygame.sprite.Sprite.update(self)

        if self.is_walking():
            self.frames_count += 1
            # obsługa zmiany klatki animacji po kilku krokach
            if self.frames_count >= self.CHANGE_ANIM_AFTER_STEPS:
                if self.frame == len(self.images_str) - 1:
                    self.frame = 0
                self.frame += 1
                self.frames_count = 0

            # ustawiamy kierunek poruszania się postaci
            if self.body.velocity[0] > 0:
                self.direction = 1
            else:
                self.direction = -1

        self.image = self.images[self.frame]

        # odbicie lustrzane klatki animacji jeśli kierunek jest odpowiedni
        if self.direction == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        
        self.rect.centerx = self.body.position[0]
        self.rect.bottom = self.body.position[1] + 40

    def is_jumping(self):
        return not self.on_ground

    def jump(self):
        if self.is_jumping():
            return
        self.body.apply_impulse(pymunk.vec2d.Vec2d(0, -4000))
        if self.is_walking():
            self.body.apply_impulse(pymunk.vec2d.Vec2d(8000 * self.direction * -1, 0))

    def walk(self, direction=1):
        if not self.is_jumping():
            self.body.velocity = pymunk.vec2d.Vec2d(500 * direction, 0)

    def is_walking(self):
        if not self.is_jumping() and self.body.velocity[0] != 0:
            return True
        return False

    def stand(self):
        pass