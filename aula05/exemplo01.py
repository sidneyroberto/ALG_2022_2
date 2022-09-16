resposta = input('Digite um número positivo: ')
n = int(resposta)
if n < 0:
    n = n * -1
elif n == 0:
    n = 1

contador = 1
while contador <= n:
    print(contador, end=' ')
    contador = contador + 1
