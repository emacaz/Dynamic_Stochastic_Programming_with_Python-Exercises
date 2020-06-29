import random
import math

def media(X):
  return sum(X) / len(X)

def varianza(X):
  mu = media(X)

  acumulador = 0
  for x in X:
    acumulador += (x - mu)**2

  return acumulador / len(X)

def desviacion_estandar(X):
  return math.sqrt(varianza(X))

if __name__ == '__main__':
  # valores del 1 al 20. El 21 no se tiene en cuenta con este método
  X = [random.randint(10, 12) for i in range(20)]
  mu = media(X)
  Var = varianza(X)
  sigma = desviacion_estandar(X)

  print(f'Arreglo X: {X}')
  print(f'Media: {mu}')
  print(f'Varianza: {Var}')
  print(f'Desviación Estándar: {sigma}')
  