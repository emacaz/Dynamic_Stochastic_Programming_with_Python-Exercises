import random
def media(X):
  return sum(X) / len(X)

if __name__ == '__main__':
  # valores del 1 al 20. El 21 no se tiene en cuenta con este método
  X = [random.randint(1, 21) for i in range(20)]
  mu = media(X)

  print(f'Lista {X}')
  print(f'Media {mu}')