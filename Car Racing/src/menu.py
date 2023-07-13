import pygame, sys
from pygame.locals import *
from sonido import *
from fondos import *
from config import *
from game import *


pygame.init()
pantalla = pygame.display.set_mode(TAMANIO_PANTALLA)
pygame.display.set_caption("Car Racing - Menu")


class Boton:
    def __init__(self, x, y, ancho, alto, texto, funcion):
        
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = COLOR_ICON
        self.texto = texto
        self.funcion = funcion
        self.game = Game()


    def dibujar(self, superficie):
        pygame.draw.rect(superficie, self.color, self.rect)
        fuente = pygame.font.Font("Car Racing/assets/fonts/SpaceMono.ttf", 25)
        texto = fuente.render(self.texto, True, (10, 10, 0))
        superficie.blit(texto, (self.rect.x + 10, self.rect.y + 2))


    def opciones(self):
        if self.funcion:
            self.funcion()

    # reproducir_melodia()


def show_menu(pantalla):
    image_fondo = pygame.transform.scale(pygame.image.load("Car Racing/assets/images/menu.png"), TAMANIO_PANTALLA)


    while True:
        manejar_eventos(botones)
        pantalla.fill((0, 0, 0))  # Limpia la pantalla con color negro
        pantalla.blit(image_fondo, (0,0))
        dibujar_botones(botones, pantalla)
        pygame.display.update()


def manejar_eventos(botones):
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == MOUSEBUTTONDOWN:
            if evento.button == 1: 
                for boton in botones:
                    if boton.rect.collidepoint(evento.pos):
                        boton.color = COLOR_ICON_SECUN
                        boton.opciones()
        elif evento.type == MOUSEBUTTONUP:
            if evento.button == 1: 
                for boton in botones:
                    if boton.rect.collidepoint(evento.pos):
                        boton.color = COLOR_ICON


def mute():
    estado = True

    def cambiar_estado():
        nonlocal estado
        if estado:
            pausar_melodia()
            estado = False
        elif not estado:
            continuar_melodia()
            estado = True

    return cambiar_estado


# def renaudar():
#     cargar_juego_guardado()
      

def jugar():
    juego = Game()
    juego.run()

def cargar_juego_guardado():
    juego_guardado = Game()
    if juego_guardado.cargar_partida():
        juego_guardado.run()
    else:
        print("No se pudo cargar la partida guardada. Se iniciará un nuevo juego.")
        juego_guardado.run()

# def cargar_juego_guardado():
#     juego_guardado = Game()
#     if juego_guardado.cargar_partida():
#         juego_guardado.run()
#     else:
#         print("No se pudo cargar la partida guardada. Se iniciará un nuevo juego.")
#         juego_guardado.run()


def dibujar_botones(botones, pantalla):
    for boton in botones:
        boton.dibujar(pantalla)


boton1 = Boton(60, 500, 200, 50, "Jugar", jugar)
boton2 = Boton(300, 500, 200, 50, "Renaudar", cargar_juego_guardado)
boton3 = Boton(550, 500, 200, 50, "Silenciar", mute())
botones = [boton1, boton2, boton3]