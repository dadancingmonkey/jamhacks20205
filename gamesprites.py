import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((50, 150, 50))
        self.rect = self.image.get_rect(center=pos)

    def update(self, dt):
        # Add movement or animation here
        pass

class Tree(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill((34, 139, 34))
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self, dt):
        pass
