import pygame
from config import *




# Clase Diamon
class Barrera(pygame.sprite.Sprite):
    def __init__(self, image, size, position, speed):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), size)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def stop(self):
        self.speed = 0