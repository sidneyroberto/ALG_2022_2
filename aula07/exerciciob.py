from random import randint

contador_sorteios = {}

for _ in range(100):
    numero_sorteado = randint(1, 10)
    if numero_sorteado in contador_sorteios:
        quantidade = contador_sorteios[numero_sorteado]
        contador_sorteios[numero_sorteado] = quantidade + 1
    else:
        contador_sorteios[numero_sorteado] = 1

'''
outro_dicionario = {}
for chave, valor in contador_sorteios.items():
    if valor % 2 == 0:
        outro_dicionario[chave] = valor

contador_sorteios = outro_dicionario
print(contador_sorteios)
'''

'''
chaves = []
for chave, valor in contador_sorteios.items():
    if valor % 2 == 1:
        chaves.append(chave)

for chave in chaves:
    del contador_sorteios[chave]

print(contador_sorteios)
'''

chaves = list(contador_sorteios.keys())
contador = 0
while contador < len(chaves):
    chave = chaves[contador]
    if contador_sorteios[chave] % 2 == 1:
        del contador_sorteios[chave]
    contador += 1

print(contador_sorteios)
