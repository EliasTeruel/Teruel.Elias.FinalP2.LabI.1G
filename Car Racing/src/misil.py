import pygame

class Misil(pygame.sprite.Sprite):
    def __init__(self, size: tuple, midbottom: tuple, color: tuple = (255, 0, 0), speed: int = 10):
        super().__init__()

        self.image = pygame.surface.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.midbottom = midbottom
        self.speed = speed


    def update(self):
        self.rect.y -= self.speed

    def stop(self):
        self.speed = 0