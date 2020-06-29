import random
import collections

# Por convención en Python se usa la variable toda en mayúscula para denotar una 'const'
PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']

# función para generar la baraja
def crear_baraja():
  barajas = []
  for palo in PALOS:
    for valor in VALORES:
      barajas.append((palo, valor))

  return barajas

def obtener_mano(barajas, tamano_mano):
  mano = random.sample(barajas, tamano_mano)

  return mano

def main(tamano_mano, intentos):
  barajas = crear_baraja()

  manos = []
  for _ in range(intentos):
    mano = obtener_mano(barajas, tamano_mano)
    manos.append(mano)

  pares = 0
  for mano in manos:
    valores = []
    for carta in mano:
      valores.append(carta[1])
    
    counter = dict(collections.Counter(valores))
    for val in counter.values():
      if val == 3:
        pares += 1
        break

  probabilidad_par = pares / intentos
  print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')

# entry point
if __name__ == '__main__':
  tamano_mano = int(input('De cuantas cartas será la mano: '))
  intentos = int(input('Y cuántos intentos para calcular la probabilidad: '))

  main(tamano_mano, intentos)