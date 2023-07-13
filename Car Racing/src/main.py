import pygame
from menu import show_menu
from config import *

pygame.init()

ventana = pygame.display.set_mode((TAMANIO_PANTALLA))
pygame.display.set_caption("Car Racing - Menu")

show_menu(ventana)


"""
ver que bajan las vidas per no las sube, debieria detectar colicion en el autito
"""