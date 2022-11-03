from random import randint


contador_sorteios = {}
range_sorteio = 10
quantidade_sorteios = 100
# Este laço vai executar quantidade_sorteios vezes
for _ in range(quantidade_sorteios):
    numero_sorteado = randint(1, range_sorteio)
    if numero_sorteado in contador_sorteios:
        quantidade = contador_sorteios[numero_sorteado]
        contador_sorteios[numero_sorteado] = quantidade + 1
    else:
        contador_sorteios[numero_sorteado] = 1
print(contador_sorteios)
