# import pygame, random
# from config import *
# from config import *

# class Fuel(pygame.sprite.Sprite):
#     def __init__(self, path_imagen, size, center):
#         super().__init__()
#         self.image = pygame.image.load(path_imagen).convert_alpha()
#         self.image = pygame.transform.scale(self.image, size)
#         self.rect = self.image.get_rect()
#         self.rect.center = center

#     def generate_fuel(self, fuels, sprites):
#         for i in range(2):
#             if i % 2 == 0:
#                 x = 290
#             else:
#                 x = 510
#             y = random.randint(-2000, ALTO // 3)
#             velocidad = random.randint(1, 2)
#             fuel = Fuel("./assets/images/fuel/bidon.png", (40, 40), (x, y))

#             collision_vida = pygame.sprite.spritecollide(fuel, fuels, False)
#             max_attempts = 10
#             while collision_vida and max_attempts > 0:
#                 y += random.choice([-1, 1]) * random.randint(1, 5)

#                 if y < 50:
#                     y = 50
#                 elif y > ALTO - 50:
#                     y = ALTO - 50

#                 fuel.rect.x = x
#                 fuel.rect.y = y
#                 collision_vida = pygame.sprite.spritecollide(fuel, fuels, False)
#                 max_attempts -= 1

#             if max_attempts > 0:
#                 fuels.add(fuel)
#                 sprites.add(fuel)

