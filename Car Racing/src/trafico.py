import pygame
from config import *

class Transito(pygame.sprite.Sprite):
    def __init__(self, path_imagen: str, size: tuple, center: tuple, speed: int = 10) -> None:
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(path_imagen).convert_alpha(), size)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = speed        

    def update(self):
        self.rect.y += self.speed

    def stop(self):
        self.speed = 0