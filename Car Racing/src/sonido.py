import pygame

def reproducir_melodia():
    pygame.mixer.init()
    pygame.mixer.music.load("Car Racing/assets/sound/sound_fondo.wav")
    pygame.mixer.music.play(-1)  # Reproducir la melodía en bucle infinito

def pausar_melodia():
    pygame.mixer.music.pause()

def continuar_melodia():
    pygame.mixer.music.unpause()

def sonido_vida():
    pygame.mixer.music.load("Car Racing/assets/sound/sound_vida.mp3")
    pygame.mixer.music.play()

def sonido_game_over():
    pygame.mixer.music.load("Car Racing/assets/sound/barrera_sound.wav")
    pygame.mixer.music.play()

def sonido_fuel():
    pygame.mixer.music.load("Car Racing/assets/sound/fuel_sound.wav")
    pygame.mixer.music.play()

def sonido_misil():
    pygame.mixer.music.load("Car Racing/assets/sound/misil.wav")
    pygame.mixer.music.play()

def sonido_pause():
    pygame.mixer.music.load("Car Racing/assets/sound/pause_sound.wav")
    pygame.mixer.music.play()

def sonido_select():
    pygame.mixer.music.load("Car Racing/assets/sound/select_sound.wav")
    pygame.mixer.music.play()



