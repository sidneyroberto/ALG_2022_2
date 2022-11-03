import imp
from random import randint

# Inline loop
numeros = [randint(1, 100) for _ in range(0, 10)]
impares = [num for num in numeros if num % 2 == 1]
'''
for _ in range(0, 10):
    num = randint(1, 100)
    numeros.append(num)
    if num % 2 == 1:
        impares.append(num)
'''

print('Lista completa de números: ', end=' ')
print(numeros)
print('Apenas os ímpares: ', end=' ')
print(impares)
