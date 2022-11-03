from random import randint

numeros = []
for _ in range(0, 10):
    num = randint(1, 100)
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)
numeros.sort()  # ordena os números
print(numeros)
print('Maior da lista: %d' % maior)
print('Menor da lista: %d' % menor)

'''
elementos = ['Rose', 'Sidney']
sorteado = randint(0, len(elementos) - 1)
print(elementos[sorteado])

num = randint(1, 60)
if num not in numeros:
'''
