import pygame, random
import sys, csv, os
from pygame.locals import *
from fondos import *
from sonido import *
from config import *
from barrera import *
from autito import *
from trafico import *
from vida import *
from diamon import *
from gameOver import *
# from guardar import *



class Boton:
    def __init__(self, x, y, ancho, alto, texto, funcion):
        
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = COLOR_ICON
        self.texto = texto
        self.funcion = funcion


    def dibujar(self, superficie):
        pygame.draw.rect(superficie, self.color, self.rect)
        fuente = pygame.font.Font("Car Racing/assets/fonts/SpaceMono.ttf", 25)
        texto = fuente.render(self.texto, True, (10, 10, 0))
        superficie.blit(texto, (self.rect.x + 10, self.rect.y + 2))


    def opciones(self):
        if self.funcion:
            self.funcion()


class Game:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode(TAMANIO_PANTALLA)
        pygame.display.set_caption("Car Racing")
        self.reloj = pygame.time.Clock()

        self.transits = pygame.sprite.Group()
        self.fondos = Fondo()
        self.auto = Jugador(self.transits)
        self.vidas = Vida()
        self.barrera = Vida()

        self.sprites = pygame.sprite.Group()
        self.autos = pygame.sprite.Group(self.auto)
        self.vids = pygame.sprite.Group()
        self.fuels = pygame.sprite.Group()
        self.diamos = pygame.sprite.Group()
        self.misils = pygame.sprite.Group()#
        self.barrers = pygame.sprite.Group()#

        self.sprites.add(self.transits)#
        self.sprites.add(self.vids)#
        self.sprites.add(self.barrers)#
        # self.sprites.add(self.diamos)#
        self.sprites.add(self.fuels)#
        self.sprites.add(self.diamos)#
        # self.sprites.add(self.auto)
        self.textos = Fondo.mostrar_start()
        self.tiempo_cambio = 120 

        self.contador_vidas = 0
        self.contador_diamantes = 0
        self.acomula_niveles = 0
        self.contador_restar_vidas = 0
        self.cantidad_transito = 1
        self.nivel = 0
        self.score = 0
        self.flag = True
        self.contador = 0
        self.colision_detectada = False
        self.colision_detec_vida = False
        self.colision_detec_fuel = False
        self.colision_detec_diamond = False
        self.colision_detec_barrera = False
        self.star_ok = False
        self.flag_up = False
        self.flag_down = False
        self.habilita = False
        self.flag_misil = False
        self.flag_contador_misil = True
        self.text_misil = "off"

        self.contador_misil = 5
       
        self.puntajes = []
        reproducir_melodia()
        self.cambio_imagen = True

        self.flag_pausa = True
        self.flag_mute = True
        self.pause = True
        self.esta_jugando = False
        self.esta_ejecutado = False
        self.esta_game_over = False
        self.melodia_reproduciendose = True
        self.melodia_pausada = False

        self.font_config = pygame.font.SysFont("Car Racing/assets/fonts/SpaceMono.ttf", 35)
        self.font_score = pygame.font.SysFont("Car Racing/assets/fonts/SpaceMono.ttf", 50)
        self.font_timer = pygame.font.SysFont("Car Racing/assets/fonts/SpaceMono.ttf", 50)
        # self.timer_fondo = pygame.USEREVENT
        # temporizador = pygame.time.set_timer(self.timer_fondo, FPS)

        self.boton1 = Boton(2, 90, 120, 40, "Menu", self.menu)
        self.boton2 = Boton(2, 150, 120, 40, "Guardar", self.guardar)
        self.boton3 = Boton(2, 210, 120, 40, "Salir", self.salir)
        self.botones = [self.boton1, self.boton2, self.boton3]
        #tiempo fuel
        self.tiempo_restante = 30
        self.tiempo_mostrado = self.tiempo_restante
        self.tiempo_inicial = pygame.time.get_ticks()
        self.tiempo_pausado = False
        self.tiempo_pausado_inicial = 0
        #tiempo general
        self.tiempo_restante_general = 3000
        self.tiempo_mostrado_general = self.tiempo_restante_general
        self.tiempo_inicial_general = pygame.time.get_ticks()
        # self.tiempo_pausado = False
        # self.tiempo_pausado_inicial = 0

        self.timer_general = pygame.time.Clock()
    def mostrar_tiempo(self):
        self.texto_tiempo = self.font_timer.render(f"Fuel: {self.tiempo_mostrado}", True, (0, 0, 0))
        self.ventana.blit(self.texto_tiempo, (650,5))
        
    def cargar_puntajes(self):
        with open('Car Racing/src/puntajes.csv', 'r') as file:
            reader = csv.reader(file)
            self.puntajes = list(reader)

    def mostrar_ranking(self, pantalla):
        fuente = pygame.font.Font("Car Racing/assets/fonts/SpaceMono.ttf", 18)
        y = 300

        for i, puntaje in enumerate(self.puntajes):
            nombre = puntaje[0]
            score = puntaje[1]
            texto = f"{i+1}. {nombre}: {score}"
            texto_surface = fuente.render(texto, True, (255, 255, 255))
            pantalla.blit(texto_surface, (632, y))
            y += 36


    def menu(self):
        print("Función del botón 1")
        
    
    # def guardar(self):

    #     coordenadas = (self.auto.rect.centerx, self.auto.rect.centery)
    #     tiempo_fuel = self.tiempo_restante
    #     diamantes_recolectados = self.contador_diamantes
    #     nivel = self.acomula_niveles + 1
    #     velocidad = self.velocidad
    #     score = self.score
    #     self.guardar_partida(coordenadas, tiempo_fuel, diamantes_recolectados, nivel, velocidad, score)
    #     # self.guarda_jugada()

    def guardar(self):
        coordenadas = (self.auto.rect.centerx, self.auto.rect.centery)
        tiempo_fuel = self.tiempo_mostrado
        diamantes_recolectados = self.contador_diamantes
        nivel = self.acomula_niveles + 1
        velocidad = self.velocidad
        score = self.score
        self.guardar_partida(coordenadas, tiempo_fuel, diamantes_recolectados, nivel, velocidad, score)
    
    
    def salir(self):
        pygame.quit()
        sys.exit()
    

    def text_config(self):
        self.texto_config1 = self.font_config.render(f"P -> Pausa", True, (0, 0, 0))
        self.texto_config2 = self.font_config.render(f"M -> Mute", True, (0, 0, 0))
        self.ventana.blit(self.texto_config1, (5, 530))
        self.ventana.blit(self.texto_config2, (5, 550))


    def run(self):
        self.esta_jugando = True # comienza el juego
        self.esta_ejecutado = True
        self.esta_game_over = False
        self.colicion = True
        self.cargar_puntajes()

        while self.esta_ejecutado:
            self.reloj.tick(FPS)
            self.handler_events()
            self.update()
            self.render()
            
            tiempo_transcurrido = (pygame.time.get_ticks() - self.tiempo_inicial) // 1000
            self.tiempo_mostrado = max(0, self.tiempo_restante - tiempo_transcurrido)

            tiempo_transcurrido_general = (pygame.time.get_ticks() - self.tiempo_inicial_general) // 1000
            self.tiempo_mostrado_general = max(0, self.tiempo_restante_general - tiempo_transcurrido_general)



    def handler_events(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1: 
                    for boton in self.botones:
                        if boton.rect.collidepoint(evento.pos):
                            boton.color = COLOR_ICON_SECUN
                            boton.opciones()

            elif evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1: 
                    for boton in self.botones:
                        if boton.rect.collidepoint(evento.pos):
                            boton.color = COLOR_ICON


            if evento.type == pygame.KEYDOWN:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        self.tiempo_restante = 30
                        self.tiempo_mostrado = self.tiempo_restante
                        self.tiempo_inicial = pygame.time.get_ticks()
                if evento.key == pygame.K_LEFT:
                    self.auto.speed_x = - VELOCIDAD_ATUTO
                    self.auto.indice = 1

                if evento.key == pygame.K_RIGHT:
                    self.auto.speed_x = VELOCIDAD_ATUTO
                    self.auto.indice = 2

                if evento.key == pygame.K_UP:
                    self.auto.speed_y = - VELOCIDAD_ATUTO
                    self.auto.indice = 3
                    self.flag_up = True
                
                if evento.key == pygame.K_DOWN:
                    self.auto.speed_y = VELOCIDAD_ATUTO
                    # self.flag_down = True

                if evento.key == pygame.K_SPACE:
                    if evento.key == pygame.K_SPACE:
                        if self.flag_misil and self.flag_contador_misil:
                            self.auto.shot(self.sprites, self.misils)
                            self.contador_misil -= 1
                            if self.contador_misil == 0:
                                self.flag_contador_misil = False
                                self.contador_misil = 5
                
                if evento.key == pygame.K_p:
                    if self.flag_pausa:
                        self.pause = False
                        self.flag_pausa = False
                    else:
                        self.pause = True
                        self.flag_pausa = True
                
                if evento.key == pygame.K_m:
                    if self.flag_mute:
                        pausar_melodia()
                        self.flag_mute = False
                    else:
                        continuar_melodia()
                        self.flag_mute = True


            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and self.auto.speed_x < 0:
                    self.auto.speed_x = 0
                    self.auto.indice = 0

                if evento.key == pygame.K_RIGHT and self.auto.speed_x > 0:
                    self.auto.speed_x = 0
                    self.auto.indice = 0

                if evento.key == pygame.K_UP and self.auto.speed_y < 0:
                    self.auto.speed_y = 0
                    self.auto.indice = 0
                    self.flag_up = False

                if evento.key == pygame.K_DOWN and self.auto.speed_y > 0:
                    self.auto.speed_y = 0    
                    self.auto.indice = 0
                    self.flag_down = True


    def update(self):
        if self.pause:


            #--- dibuja el fondo con la cuenta regresiva ---#
            self.fondos.dibujar(self.ventana)
            self.star_ok = Fondo.update_start(self.textos, ALTO, ANCHO, self.ventana)
            if self.star_ok == True and self.cambio_imagen:
                self.cambio_imagen = False
            if not self.cambio_imagen:
                self.tiempo_acumulado += self.reloj.get_time()

                if self.tiempo_acumulado >= self.tiempo_cambio:
                    self.habilita = True

                    self.tiempo_acumulado = 0
            else:
                self.tiempo_acumulado = 0
        #---- fin ----#

            if self.habilita:
                self.sprites.update() 
                self.fondos.cambiar_imagen()
                self.sprites.update() 
                self.fondos.dibujar(self.ventana)  
                self.generate_fuel()
                self.generate_diamond()

                self.generate_transits()
                self.generate_vidas()
                self.auto.update(self.ventana) 
                self.mostrar_tiempo()
                self.mostrar_ranking(self.ventana)
            for boton in self.botones:
                boton.dibujar(self.ventana)

            self.detec_colicion()    
            self.show_score()
            self.text_config()
            self.borra_elementos()
            self.show_niveles()
            
            self.diamos.update()
            
    def render(self):
        if self.esta_game_over:
            # self.show_game_over()
            pass
        elif self.esta_jugando:
            self.sprites.draw(self.ventana) 
            self.fuels.draw(self.ventana)
            self.autos.draw(self.ventana)
            self.diamos.draw(self.ventana)
            self.flag = True

        pygame.display.flip()


    def generate_transits(self):
        images = ["Car Racing/assets/images/autos/car0.png", "Car Racing/assets/images/autos/car1.png", 
                  "Car Racing/assets/images/autos/car2.png","Car Racing/assets/images/autos/car3.png"]

        if self.acomula_niveles == 0:
            self.velocidad = 1
        elif self.acomula_niveles == 1:
            self.velocidad = 2
            self.generate_barrera()
            self.cantidad_transito = 2
            self.flag_misil = True
        elif self.acomula_niveles == 2:
            self.velocidad = 2
            self.cantidad_transito = 3
            self.generate_barrera()
            self.flag_misil = True

        elif self.acomula_niveles == 3:

            self.velocidad = 3
            self.cantidad_transito = 4
            self.generate_barrera()
            self.flag_misil = True
            
        
        if len(self.transits) == 0:
            for i in range(self.cantidad_transito):

                if i % 2 == 0:
                    x = 290  
                else:
                    x = 510  
                y = random.randint(-1500, ALTO // 3)
                image = images[i % len(images)]
                transito = Transito(image, SIZE_TRANSITS, (x, y), self.velocidad)
                collision = pygame.sprite.spritecollide(transito, self.transits, True)
                max_intentos = 10 
                while collision and max_intentos > 0:
                    y += -1 * random.randint(2, 6) 
                    transito.rect.center = (x, y)
                    max_intentos -= 1

                if max_intentos > 0:  
                    self.transits.add(transito)
                    self.sprites.add(transito)


    def generate_vidas(self):
        image = "Car Racing/assets/images/vidas/vida0.png"
            
        for i in range(4):
                if i % 2 == 0:
                    x = 290  
                else:
                    x = 510 
                y = random.randint(-1000, ALTO // 3)
                velocidad = 1
                select_imagen = random.randint(1,3000)
                if select_imagen == 150:
                    self.vida_juego = Vida_juego(image, (30,30), (x, y), velocidad)

                    collision_vida = pygame.sprite.spritecollide(self.vida_juego, self.vids, True)
                    max_intentos = 10  
                    while collision_vida and max_intentos > 0:
                        y += random.choice([-1, 1]) * random.randint(1, 5)  
                        self.vida_juego.rect.center = (x, y)
                        collision_vida = pygame.sprite.spritecollide(self.vida_juego, self.vids, True)
                        max_intentos -= 1

                    if max_intentos > 0:  # Si se encontró una posición no colisionante
                        self.vids.add(self.vida_juego)
                        self.sprites.add(self.vida_juego)


    def generate_fuel(self):
        image = "Car Racing/assets/images/fuel/bidon.png"
            
        for i in range(2):
                if i % 2 == 0:
                    x = 290 
                else:
                    x = 510  
                y = random.randint(-1000, ALTO // 3)
                velocidad = 1
                select_imagen = random.randint(1,3000)
                if select_imagen == 350:
                    self.fuel = Fuel(image, (30,30), (x, y), velocidad)

                    collision_fuel = pygame.sprite.spritecollide(self.fuel, self.fuels, True)
                    max_intentos = 10  
                    while collision_fuel and max_intentos > 0:
                        y += random.choice([-1, 1]) * random.randint(1, 5)  
                        self.fuel.rect.center = (x, y)
                        max_intentos -= 1

                    if max_intentos > 0: 
                        self.fuels.add(self.fuel)
                        self.sprites.add(self.fuel)


    def generate_diamond(self):
        image = "Car Racing/assets/images/diamon/diamante.png"

        for i in range(2):
            if i % 2 == 0:
                x = 290
            else:
                x = 510
            y = random.randint(-1000, ALTO // 3)
            velocidad = 1
            select_image = random.randint(1, 3100)
            if select_image == 750:
                self.diamante = Diamon(image, (50, 50), (x, y), velocidad)

                collision_diamante = pygame.sprite.spritecollide(self.diamante, self.diamos, True)
                max_attempts = 10
                while collision_diamante and max_attempts > 0:
                    y += random.choice([-1, 1]) * random.randint(1, 5)
                    self.diamante.rect.center = (x, y)
                    max_attempts -= 1

                if max_attempts > 0:  
                    self.diamos.add(self.diamante)
                    self.sprites.add(self.diamante)


    def generate_barrera(self):
        image = "Car Racing/assets/images/barrera/barrera.png"

        x = (ANCHO // 2) + 13
        y = random.randint(-2000, ALTO // 3)
        velocidad = 1
        select_image = random.randint(1, 1100)
        if select_image == 50:
            self.barrera = Barrera(image, (110, 20), (x, y), velocidad)

            collision_barrera = pygame.sprite.spritecollide(self.barrera, self.barrers, True)
            max_attempts = 10
            while collision_barrera and max_attempts > 0:
                y += random.choice([-1, 1]) * random.randint(1, 5)
                self.barrera.rect.center = (x, y)
                max_attempts -= 1

            if max_attempts > 0:  # Si se encontró una posición no colisionante
                self.barrers.add(self.barrera)
                self.sprites.add(self.barrera)


    def show_niveles(self):
        if self.contador_diamantes == 3:
            self.nivel = 1
            self.acomula_niveles += 1
            self.contador_diamantes = 0

        self.texto_tiempo = self.font_timer.render(f"Nivel: {self.acomula_niveles + 1}", True, (0, 0, 0))
        self.ventana.blit(self.texto_tiempo, (650,65))
        self.texto_tiempo = self.font_timer.render(f"X {self.contador_diamantes}", True, (0, 0, 0))
        self.ventana.blit(self.texto_tiempo, (725,120))
        self.image_diamante = pygame.transform.scale(pygame.image.load("Car Racing/assets/images/diamon/diamante.png").convert_alpha(), (50,50))
        self.ventana.blit(self.image_diamante, (660,110))

        if self.flag_misil and self.contador_misil > 0 and self.flag_contador_misil:
            self.texto_tiempo = self.font_timer.render(f"Misil: {self.contador_misil}", True, (0, 0, 0))
            self.ventana.blit(self.texto_tiempo, (650, 170))
        else:
            self.texto_tiempo = self.font_timer.render(f"Misil: {self.text_misil}", True, (0, 0, 0))
            self.ventana.blit(self.texto_tiempo, (650, 170))
                

    def borra_elementos(self):
        for transito in self.transits:
            if transito.rect.top >= ALTO:
                self.score += 100
                transito.kill()
                self.show_score()
        for misil in self.misils:
            if misil.rect.bottom <= 0:
                misil.kill()
        for vid in self.vids:
            if vid.rect.top >= ALTO:
                vid.kill()
        for diams in self.diamos:
            if diams.rect.top >= ALTO:
                diams.kill()
        for full in self.fuels:
            if full.rect.top >= ALTO:
                full.kill()
        for barr in self.barrers:
            if barr.rect.top >= ALTO:
                barr.kill()
        
            
    def detec_colicion(self):
        colisiones = pygame.sprite.spritecollide(self.auto, self.transits, False)
        if colisiones and not self.colision_detectada:
            # self.vidas.restar_vida(self.ventana)
            
            # print("SDFDF")
            self.contador_restar_vidas += 1
            if self.contador_restar_vidas == 4:
                self.mostrar_game_over()
                sonido_game_over()
                self.colision_detectada = True
            elif not colisiones and self.colision_detectada:
                self.colision_detectada = False

        # colisions_vida = pygame.sprite.spritecollide(self.auto, self.vids, False)
        # if colisions_vida and not self.colision_detec_vida:
        #     self.vidas.sumar_vida(self.ventana)
        #     sonido_vida()
        #     self.vida_juego.kill()
        #     # self.vidas.kill()
        #     self.contador_vidas += 1
        #     self.contador_restar_vidas -= 1
        #     self.colision_detec_vida = True
        # elif not colisions_vida and self.colision_detec_vida:
        #     self.colision_detec_vida = False
            
        # colisions_fuel = pygame.sprite.spritecollide(self.auto, self.fuels, False)
        # if colisions_fuel and not self.colision_detec_fuel:
        #     self.fuel.kill()
        #     sonido_fuel()
        #     self.tiempo_restante = 30
        #     self.tiempo_mostrado = self.tiempo_restante
        #     self.tiempo_inicial = pygame.time.get_ticks()
        #     self.colision_detec_fuel = True
        # elif not colisions_fuel and self.colision_detec_fuel:
        #     self.colision_detec_fuel = False

        colisions_vida = pygame.sprite.spritecollide(self.auto, self.vids, True)
        for i in colisions_vida:
            self.vidas.sumar_vida(self.ventana)
            sonido_vida()
            self.vida_juego.kill()
            # self.vidas.kill()
            self.contador_vidas += 1
            self.contador_restar_vidas -= 1
            self.colision_detec_vida = True
            self.sprites.add(self.vids)
       

        colisions_fuel = pygame.sprite.spritecollide(self.auto, self.fuels, True)
        for i in colisions_fuel:
        # if colisions_fuel and not self.colision_detec_fuel:
            self.fuel.kill()
            sonido_fuel()
            self.tiempo_restante = 30
            self.tiempo_mostrado = self.tiempo_restante
            self.tiempo_inicial = pygame.time.get_ticks()
            self.colision_detec_fuel = True
            self.sprites.add(self.fuels)
        # elif not colisions_fuel and self.colision_detec_fuel:
        #     self.colision_detec_fuel = False
        
        # colisions_diamond = pygame.sprite.spritecollide(self.auto, self.diamos, False)
        # if colisions_diamond and not self.colision_detec_diamond:
        #     self.diamante.kill()
        #     self.contador_diamantes += 1
        #     if self.contador_diamantes == 3:
        #         self.flag_contador_misil = True
            
        #     self.colision_detec_diamond = True
        # elif not colisions_diamond and self.colision_detec_diamond:
        #     self.colision_detec_diamond = False
        
        lista = pygame.sprite.spritecollide(self.auto, self.diamos, True) 
        for i in lista:
            # if not self.colision_detec_diamond:
                self.diamante.kill()
                self.sprites.add(self.diamos)
                self.contador_diamantes += 1
                if self.contador_diamantes == 3:
                    self.flag_contador_misil = True
                
            #     self.colision_detec_diamond = True
            # elif self.colision_detec_diamond:
            #     self.colision_detec_diamond = False

        colisions_barrers = pygame.sprite.spritecollide(self.auto, self.barrers, False)
        if colisions_barrers and not self.colision_detec_barrera:
            self.barrera.kill()
            sonido_game_over()
            self.mostrar_game_over()            
            self.colision_detec_barrera = True
        elif not colisions_barrers and self.colision_detec_barrera:
            self.colision_detec_barrera = False

        for misil in self.misils:
            lista = pygame.sprite.spritecollide(misil, self.transits, True)
            if len(lista) != 0:
                misil.kill()
                self.score += 250



    def mostrar_game_over(self):
        show_game_over(self, self.ventana)

    # def guardar_partida(self, coordenadas, tiempo_fuel, diamantes_recolectados, nivel, velocidad, score):
    #     ruta_archivo = 'Car Racing/src/partida.csv'
    #     existe_archivo = os.path.isfile(ruta_archivo)

    #     with open(ruta_archivo, 'a', newline='') as archivo:
    #         escritor = csv.writer(archivo)
    #         if not existe_archivo:
    #             escritor.writerow(['Coordenada X', 'Coordenada Y', 'tiempo', 'diamantes'])
    #         escritor.writerow([coordenadas[0], coordenadas[1], tiempo_fuel, diamantes_recolectados, nivel, velocidad, score])


    def guardar_partida(self, coordenadas, tiempo_fuel, diamantes_recolectados, nivel, velocidad, score):
        ruta_archivo = 'Car Racing/src/partida.csv'
        existe_archivo = os.path.isfile(ruta_archivo)

        with open(ruta_archivo, 'a', newline='') as archivo:
            escritor = csv.writer(archivo)
            if not existe_archivo:
                escritor.writerow(['Coordenada X', 'Coordenada Y', 'Tiempo Fuel', 'Diamantes Recolectados', 'Nivel', 'Velocidad', 'Puntuación'])
            escritor.writerow([coordenadas[0], coordenadas[1], tiempo_fuel, diamantes_recolectados, nivel, velocidad, score])



    def cargar_partida(self):
        ruta_archivo = 'Car Racing/src/partida.csv'
        if not os.path.isfile(ruta_archivo):
            print("No hay partidas guardadas.")
            return False

        with open(ruta_archivo, 'r') as archivo:
            lector = csv.reader(archivo)
            lineas = list(lector)
            if len(lineas) < 2:
                print("No hay partidas guardadas.")
                return False

            coordenada_x = int(lineas[-1][0])
            coordenada_y = int(lineas[-1][1])
            tiempo_fuel = int(lineas[-1][2])
            diamantes_recolectados = int(lineas[-1][3])
            nivel = int(lineas[-1][4])
            velocidad = int(lineas[-1][5])
            score = int(lineas[-1][6])
            self.auto.rect.centerx = coordenada_x
            self.auto.rect.centery = coordenada_y
            self.tiempo_restante = tiempo_fuel
            self.contador_diamantes = diamantes_recolectados
            self.acomula_niveles = nivel - 1
            self.velocidad = velocidad
            self.score = score
            return True


    # def cargar_partida(self):
    #     ruta_archivo = 'Car Racing/src/jugadas.csv'
    #     if not os.path.isfile(ruta_archivo):
    #         print("No hay partidas guardadasascsc.")
    #         return False

    #     with open(ruta_archivo, 'r') as archivo:
    #         lector = csv.reader(archivo)
    #         lineas = list(lector)
    #         if len(lineas) < 2:
    #             print("No hay partidas guardadas.")
    #             return False

    #         coordenada_x = int(lineas[-1][0])
    #         coordenada_y = int(lineas[-1][1])
    #         tiempo_fuel = int(lineas[-1][2])
    #         diamantes_recolectados = int(lineas[-1][3])
    #         nivel = int(lineas[-1][4])
    #         velocidad = int(lineas[-1][5])
    #         score = int(lineas[-1][6])
    #         self.auto.rect.centerx = coordenada_x
    #         self.auto.rect.centery = coordenada_y
    #         self.tiempo_restante = tiempo_fuel
    #         self.contador_diamantes = diamantes_recolectados
    #         self.acomula_niveles = nivel -1
    #         self.velocidad = velocidad
    #         self.score = score


    def show_score(self):
        self.texto_score = self.font_score.render(f"score: {self.score}", True, (0, 0, 0))
        self.ventana.blit(self.texto_score, (0,0))
    

    def game_over(self):
        self.esta_jugando = False 
        self.esta_game_over = True

    def restart_game(self):
        self.score = 0
        for i in range(3):
            self.vidas.sumar_vida(self.ventana)
        self.sprites.empty()
        self.tiempo_total = 30
        self.tiempo_restante = self.tiempo_total
        self.contador_vidas = 0
        self.transits.empty()
        self.fuels.empty()
        self.auto.reset()
        self.misils.empty()
        self.sprites.add(self.auto)
        self.run()

if __name__ == "__main__":
    game = Game()
    game.run()