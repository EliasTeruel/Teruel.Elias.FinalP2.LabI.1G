import pygame
from config import *

SIZE_START = 130
SPEED_START = 8
POS_START = 350
COLOR_START =(255, 150, 0)
# VELOCIDAD_CAMBIO = 1 # Valor de ejemplo, puedes ajustarlo según tus necesidades


class Fondo:
    def __init__(self):
        self.imagenes = ['Car Racing/assets/images/pista/pista0.png', 'Car Racing/assets/images/pista/pista1.png', 
                         'Car Racing/assets/images/pista/pista2.png']
        self.indice = 0
        self.cargar_imagen()

    def cargar_imagen(self):
        self.imagen_actual = pygame.image.load(self.imagenes[self.indice]).convert()
        self.imagen_actual = pygame.transform.scale(self.imagen_actual, TAMANIO_PANTALLA)

    def cambiar_imagen(self):
        self.indice = (self.indice + 1) % len(self.imagenes)
        self.cargar_imagen()

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen_actual, (0, 0))


    def mostrar_start():
        text_data = [
            {"text": "3", "font_size": SIZE_START, "color": COLOR_START, "speed": SPEED_START, "enabled": True, "y_pos": POS_START},
            {"text": "2", "font_size": SIZE_START, "color": COLOR_START, "speed": SPEED_START, "enabled": False, "y_pos": POS_START},
            {"text": "1", "font_size": SIZE_START, "color": COLOR_START, "speed": SPEED_START, "enabled": False, "y_pos": POS_START},
            {"text": "START!", "font_size": SIZE_START, "color": COLOR_START, "speed": SPEED_START, "enabled": False, "y_pos": POS_START}
        ]
        return text_data


    def update_start(textos, width, height, pantalla)-> bool:
        flag = False
        for i, text_entry in enumerate(textos):
            text = text_entry["text"]
            font_size = text_entry["font_size"]
            color = text_entry["color"]
            speed = text_entry["speed"]
            enabled = text_entry["enabled"]
            y_pos = text_entry["y_pos"]

            if enabled:
                font = pygame.font.Font(None, font_size)
                text_surface = font.render(text, True, color)
                text_rect = text_surface.get_rect(center=(400, y_pos))

                pantalla.blit(text_surface, text_rect)

                text_entry['y_pos'] = y_pos + speed

                if text_entry['y_pos'] > height:
                    text_entry['enabled'] = False

                    if i < len(textos) - 1:
                        textos[i + 1]['enabled'] = True
                    else:
                        print("¡Todos los textos han llegado al final!")
                        flag = True
        return flag 
