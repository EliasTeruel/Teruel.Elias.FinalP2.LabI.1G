import pygame, sys
from config import *
from vida import *
from misil import *
from gameOver import *
from sonido import *

class Jugador(pygame.sprite.Sprite):
    def __init__(self, transits):
        super().__init__()

        self.image_autos = [pygame.transform.scale(pygame.image.load("Car Racing/assets/images/autos/auto/auto1.png").convert_alpha(), TAMAÑO_AUTOS),
                            pygame.transform.scale(pygame.image.load("Car Racing/assets/images/autos/auto/auto2.png").convert_alpha(), TAMAÑO_AUTOS),
                            pygame.transform.scale(pygame.image.load("Car Racing/assets/images/autos/auto/auto3.png").convert_alpha(), TAMAÑO_AUTOS),
                            pygame.transform.scale(pygame.image.load("Car Racing/assets/images/autos/auto/auton1.png").convert_alpha(), TAMAÑO_AUTOS),
                            pygame.transform.scale(pygame.image.load("Car Racing/assets/images/autos/auto/auton2.png").convert_alpha(), TAMAÑO_AUTOS),
                            pygame.transform.scale(pygame.image.load("Car Racing/assets/images/autos/auto/auton3.png").convert_alpha(), TAMAÑO_AUTOS)
                            ]
        self.font = pygame.font.SysFont("Car Racing/assets/fonts/SpaceMono.ttf", 50)
        self.indice = 0
        self.image = self.image_autos[self.indice]
        self.rect = self.image.get_rect()
        self.rect.centerx = (ANCHO // 2) + 5 
        self.speed_x = 0 
        self.speed_y = 0 
        self.playing = True 
        self.saltando = False
        self.salto = 0
        self.left = True
        self.rect.center = START_POS
        self.resize_counter = 0  # Contador para el cambio de tamaño
        self.resize_direction = 1  # Dirección del cambio de tamaño (+1 para ampliar, -1 para reducir)
        self.original_image = self.image_autos[self.indice]  # Guarda la imagen original
        self.resized_image = self.original_image  # Imagen actualizada durante el cambio de tamaño
        self.transits = transits  # Guarda la referencia a la lista de transits
        self.imagen_colision = pygame.transform.scale(pygame.image.load("Car Racing/assets/images/autos/explosion.png").convert_alpha(), (90, 90))
        self.vidas = Vida()
        self.vids = pygame.sprite.Group(self.vidas)
        self.colision_detec_vida = False

        self.contar_vidas = 0
        self.contador_vidas = 0
        self.contador_restar_vidas = 0

        # self.vidas_restantes = 3
        self.reloj = pygame.time.Clock()


    def update(self, pantalla): #es la actualizacion del movimiento
        self.cuenta_vidas = self.contar_vidas
        # print(self.cuenta_vidas)
        if self.playing:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

        if self.rect.left <= LIMIT_IZQ:
            self.rect.left = LIMIT_IZQ
        elif self.rect.right >= LIMIT_DER:
            self.rect.right = LIMIT_DER
        
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= LIMIT_BOTTON:
            self.rect.bottom = LIMIT_BOTTON
        
        self.image = self.image_autos[self.indice]

        # Verificar colisiones con el tráfico
        colisiones = pygame.sprite.spritecollide(self, self.transits, False)
        self.vidas.cambiar_image_vida(pantalla)

        if colisiones:
            for colision in colisiones:
                # if self.vidas_restantes > 0:
                #     self.vidas_restantes -= 1

                if self.speed_x > 0 and colision.rect.left < self.rect.right:
                    self.speed_x = 0
                    self.rect.right = colision.rect.left
                    pantalla.blit(self.imagen_colision, (self.rect.x, self.rect.y))
                    self.rect.centerx = ANCHO // 2 
                    self.vidas.restar_vida(pantalla)
                    self.contar_vidas += 1
                elif self.speed_x < 0 and colision.rect.right > self.rect.left:
                    self.speed_x = 0
                    self.rect.left = colision.rect.right              
                    pantalla.blit(self.imagen_colision, (self.rect.x, self.rect.y))
                    self.rect.centerx = ANCHO // 2 
                    self.vidas.restar_vida(pantalla)
                    self.contar_vidas += 1
                if self.speed_y > 0 and colision.rect.top < self.rect.bottom:
                    self.speed_y = 0
                    self.rect.bottom = colision.rect.top
                    pantalla.blit(self.imagen_colision, (self.rect.x-10, self.rect.y+17))
                    self.rect.centerx = ANCHO // 2 
                    self.vidas.restar_vida(pantalla)
                    self.contar_vidas += 1
                elif self.speed_y < 0 and colision.rect.bottom > self.rect.top:
                    self.speed_y = 0
                    self.rect.top = colision.rect.bottom  
                    pantalla.blit(self.imagen_colision, (self.rect.x-10, self.rect.y-20))
                    self.rect.centerx = ANCHO // 2 
                    self.vidas.restar_vida(pantalla)
                    self.contar_vidas += 1


        # colisions_vida = pygame.sprite.spritecollide(self, self.vids, False)
        # if colisions_vida and not self.colision_detec_vida:
        #     self.vidas.sumar_vida(pantalla)
        #     sonido_vida()
        #     # self.vida_juego.kill()
        #     self.vidas.kill()
        #     self.contador_vidas += 1
        #     self.contador_restar_vidas -= 1
        #     self.colision_detec_vida = True
        # elif not colisions_vida and self.colision_detec_vida:
        #     self.colision_detec_vida = False

        if self.cuenta_vidas > 3:
            print("aca")
            show_game_over(self, pantalla)

            

    def reset(self):
        self.rect.center = (START_POS)
        self.speed_x = 0
        self.speed_y = 0
        # self.vidas_restantes = 3

    def stop(self): 
        self.playing = False

    def resize_image(self):
        if self.resize_counter >= 3: 
            self.resize_counter = 0 
            self.resize_direction *= -1  
            self.resized_image = self.original_image  
        else:
            scale_factor = 1 + self.resize_counter * 0.25  
            new_width = int(self.original_image.get_width() * scale_factor)
            new_height = int(self.original_image.get_height() * scale_factor)
            self.resized_image = pygame.transform.smoothscale(self.original_image, (new_width, new_height))
            self.resize_counter += 1  
        self.image = self.resized_image

    def shot(self, sprites, misils): 
        if self.playing:
            misil = Misil(SIZE_MISIL, self.rect.midtop, COLOR_MISIL, SPEED_MISIL)
            sonido_misil()
            sprites.add(misil)
            misils.add(misil)
