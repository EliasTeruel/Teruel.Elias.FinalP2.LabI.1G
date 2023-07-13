import pygame, sys
from config import *






def show_game_over(self, pantalla):
    font = pygame.font.SysFont("Car Racing/assets/fonts/SpaceMono.ttf", 50)
    fondo_game_over = pygame.surface.Surface(TAMANIO_PANTALLA)
    fondo_game_over.fill(BLACK)
    texto = font.render("Game Over", True, (0, 255, 0))
    texto_rect = texto.get_rect()
    texto_rect.center = CENTRO_PANTALLA
    pantalla.blit(fondo_game_over, ORIGIN)
    pantalla.blit(texto, texto_rect)
    pygame.display.flip()
    pygame.time.delay(2000)
    show_start_screen(self, pantalla)


def show_start_screen(self, pantalla):
    flag = True
    font = pygame.font.SysFont("Car Racing/assets/fonts/SpaceMono.ttf", 50)

    while flag:
        # self.reloj.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    flag = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        fondo_game_over = pygame.surface.Surface(TAMANIO_PANTALLA)
        fondo_game_over.fill(BLACK)
        
        texto = font.render("'q'->Salir..'s'->Reiniciar ", True, (0, 255, 0))
        texto_rect = texto.get_rect()
        texto_rect.center = CENTRO_PANTALLA
        pantalla.blit(fondo_game_over, ORIGIN)
        pantalla.blit(texto, texto_rect)
        pygame.display.flip()