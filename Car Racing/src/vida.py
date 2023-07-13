import pygame
vidas_restantes = 3
class Vida(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_vida = [
            ('Car Racing/assets/images/vidas/vida0.png', (5, 50)),
            ('Car Racing/assets/images/vidas/vida1.png', (45, 50)),
            ('Car Racing/assets/images/vidas/vida2.png', (85, 50))
        ]
        # self.vidas_restantes = 3
        self.image = pygame.transform.scale(pygame.image.load('Car Racing/assets/images/vidas/vida0.png').convert_alpha(), (40,40))
        self.rect = self.image.get_rect()
        self.cargar_imagenes()

    def cargar_imagenes(self):
        self.imagenes = []
        for image_path, position in self.image_vida:
            imagen = pygame.image.load(image_path).convert_alpha()
            imagen = pygame.transform.scale(imagen, (40, 40))
            self.imagenes.append((imagen, position))

    def cambiar_image_vida(self, screen):
        for imagen, position in self.imagenes:
            print("imagen")
            print(imagen)
            print("position")
            print(position)
            screen.blit(imagen, position)

    # def dibujar_vida(self, screen):
    #     screen.blit(self.imagen_actual, (0, 0))

    def restar_vida(self, screen):
        global vidas_restantes
        print(vidas_restantes)

        if vidas_restantes > 0:
            vidas_restantes -= 1
            self.imagenes.pop()
            self.cambiar_image_vida(screen)

    def sumar_vida(self, screen):
        global vidas_restantes
        if vidas_restantes < 3:
            vidas_restantes += 1
            last_image_path, last_position = self.image_vida[vidas_restantes - 1]
            imagen = pygame.image.load(last_image_path).convert_alpha()
            imagen = pygame.transform.scale(imagen, (40, 40))
            self.imagenes.append((imagen, last_position))
            self.cambiar_image_vida(screen)

    


class Vida_juego(pygame.sprite.Sprite):
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


class Fuel(pygame.sprite.Sprite):
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






