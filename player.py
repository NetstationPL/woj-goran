# -*- coding: utf-8 -*-
import pygame
import pymunk


class Player(pygame.sprite.Sprite):
    image = pygame.image.load("images/player_idle.png")
    images_str = ["images/player_idle.png", "images/player_walk1.png", "images/player_walk2.png", "images/player_walk3.png", ]
    default_groups = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.default_groups)

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.walk = 0
        self.frame = 0
        self.images = []
        for i in self.images_str:
            self.images.append(pygame.image.load(i))
        self.frames_count = 0
        self.CHANGE_ANIM_AFTER_STEPS = 5
        self.direction = 1
        self.body.pymunk.Body(30, pymunk.moment_for_box(50, 100, 128))
        self.body.position = (self.rect.centerx, self.rect.centery)

    def update(self):
        pygame.sprite.Sprite.update(self)

        if self.walk:
            self.frames_count += 1
            # obsługa zmiany klatki animacji po kilku krokach
            if self.frames_count >= self.CHANGE_ANIM_AFTER_STEPS:
                if self.frame == len(self.images_str) - 1:
                    self.frame = 0
                self.frame += 1
                self.frames_count = 0

            # ustawiamy kierunek poruszania się postaci
            if self.walk > 0:
                self.direction = 1
            else:
                self.direction = -1

        self.image = self.images[self.frame]

        # odbicie lustrzane klatki animacji jeśli kierunek jest odpowiedni
        if self.direction == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect.x += self.walk

        self.rect.centery = self.body.position[1]
