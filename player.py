import pygame


class Player(pygame.sprite.Sprite):
    image = pygame.image.load("images/player_idle.png")
    images_str = ["images/player_idle.png", "images/player_walk1.png", "images/player_walk2.png", "images/player_walk3.png", ]
    default_groups = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.default_groups)

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.walk = False
        self.frame = 0
        self.images = []
        for i in self.images_str:
            self.images.append(pygame.image.load(i))
        self.frames_count = 0
        self.CHANGE_ANIM_AFTER_STEPS = 5

    def update(self):
        pygame.sprite.Sprite.update(self)

        if self.walk:
            self.frames_count += 1
            if self.frames_count >= self.CHANGE_ANIM_AFTER_STEPS:
                if self.frame == len(self.images_str) - 1:
                    self.frame = 0
                self.frame += 1
                self.frames_count = 0

        self.image = self.images[self.frame]
