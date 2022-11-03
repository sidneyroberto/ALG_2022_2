from collections import OrderedDict
from random import randint

contador_sorteios = {}

for _ in range(100):
    numero_sorteado = randint(1, 10)
    if numero_sorteado in contador_sorteios:
        quantidade = contador_sorteios[numero_sorteado]
        contador_sorteios[numero_sorteado] = quantidade + 1
    else:
        contador_sorteios[numero_sorteado] = 1

lista_ordenada = sorted(contador_sorteios.items())
contador_ordenado = OrderedDict(lista_ordenada)
print(contador_ordenado)
