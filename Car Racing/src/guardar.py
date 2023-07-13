import csv

def guardar_jugada(coordenadas, tiempo_fuel, diamantes_recolectados, nivel, velocidad, score):
    ruta_archivo = 'jugadas.csv'
    existe_archivo = csv.reader(open(ruta_archivo, 'r'))

    with open(ruta_archivo, 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        if not existe_archivo:
            escritor.writerow(['Coordenada X', 'Coordenada Y', 'Tiempo de Fuel', 'Diamantes Recolectados', 'Nivel', 'Velocidad', 'Score'])
        escritor.writerow([coordenadas[0], coordenadas[1], tiempo_fuel, diamantes_recolectados, nivel, velocidad, score])

def leer_jugadas():
    ruta_archivo = 'jugadas.csv'
    jugadas = []
    with open(ruta_archivo, 'r') as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Saltar la primera fila (encabezados)
        for fila in lector:
            jugada = {
                'coordenadas': (int(fila[0]), int(fila[1])),
                'tiempo_fuel': int(fila[2]),
                'diamantes_recolectados': int(fila[3]),
                'nivel': int(fila[4]),
                'velocidad': int(fila[5]),
                'score': int(fila[6])
            }
            jugadas.append(jugada)
    return jugadas
