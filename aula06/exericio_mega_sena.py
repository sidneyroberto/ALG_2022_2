from random import randint

numeros = []
contador = 0
while contador < 6:
    num = randint(1, 60)
    if num not in numeros:
        numeros.append(num)
        contador += 1

print('Números sorteados: ', end=' ')
numeros.sort()
print(numeros)
