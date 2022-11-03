from random import randint

resposta = input('Digite a quantidade de números: ')
quantidade = int(resposta)

numeros = []
numero = randint(1, 100)
numeros.append(numero)
for i in range(0, quantidade - 1):
    while numero in numeros:
        numero = randint(1, 100)
    numeros.append(numero)

print(numeros)
for i in range(0, int(quantidade / 2)):
    inicio = i
    fim = quantidade - i
    maior = max(numeros[inicio: fim + 1])
    menor = min(numeros[inicio: fim + 1])
    numeros.remove(maior)
    numeros.remove(menor)
    numeros = numeros[0: inicio] + [maior] + \
        numeros[inicio: fim - 1] + [menor] + numeros[fim - 1:]
print(numeros)
