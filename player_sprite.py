# -*- coding: utf-8 -*-

import datetime

import pygame


class PlayerSprite(pygame.sprite.Sprite):

    image = None

    images = [[pygame.image.load("images/player_idle.png"), ],
              [pygame.image.load("images/player_walk1.png"),
               pygame.image.load("images/player_walk2.png"),
               pygame.image.load("images/player_walk3.png"),
               ]]

    def get_state(self):
        return self._state

    def set_state(self, state):
        if state != self._state:
            self.frame = 0
            self.reset_last_frame_time()
        self._state = state

    state = property(get_state, set_state)

    def __init__(self, body):
        pygame.sprite.Sprite.__init__(self)

        self.body = body

        self.frame = 0
        self.direction = 1

        self._state = 0
        self.reset_last_frame_time()

        self.image = self.images[0][0]

        self.rect = self.image.get_rect()
        self.rect.x = body.position[0]
        self.rect.y = body.position[1]

    def update(self):
        pygame.sprite.Sprite.update(self)

        if self.is_time_to_change_frame():
            self.change_frame()

        self.image = self.get_current_frame()
        self.change_direction()

        if self.direction == -1:
            self.image = pygame.transform.flip(self.image, True, False)

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

        self.rect.x = self.body.position[0]
        self.rect.y = self.body.position[1]

    def is_time_to_change_frame(self):
        last_frame_delta = datetime.datetime.now() - self.last_frame_time
        time_delta_ms = last_frame_delta.total_seconds() * 1000
        animation_speed = self.get_animation_speed()
        return bool(animation_speed and time_delta_ms > animation_speed)

    def change_frame(self):
            self.frame += 1

            if self.frame == len(self.images[self.state]):
                self.frame = 0
            self.reset_last_frame_time()

    def get_current_frame(self):
        return self.images[self.state][self.frame]

    def get_animation_speed(self):
        if self.body.velocity[0] != 0:
            # ile pixeli ma zajac cala animacja (dwa razy rozmiar sprite'a)
            animation_px = self.rect.width
            animation_time = animation_px / abs(self.body.velocity[0]) * 1000

            return animation_time / len(self.images[self.state])
        return 0

    def reset_last_frame_time(self):
        self.last_frame_time = datetime.datetime.now()

    def change_direction(self):
        if self.body.velocity[0] > 0:
            self.direction = 1
        if self.body.velocity[0] < 0:
            self.direction = -1
