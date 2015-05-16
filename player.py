import pygame

class Player(pygame.sprite.Sprite):
    image = pygame.image.load("images/player_idle.png")
    default_groups = []
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.default_groups)
            
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
