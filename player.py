import pygame

class Player(pygame.sprite.Sprite):
    image = pygame.image.load("images/player_idle.png")
    images_str = ["images/player_idle.png", "images/player_walk1.png", "images/player_walk2.png", "images/player_walk3.png",] 
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

    def update(self):
        pygame.sprite.Sprite.update(self)
        if self.walk:
            if self.frame == 3:
                self.frame = 0
            self.frame += 1
        self.image = self.images[self.frame]
