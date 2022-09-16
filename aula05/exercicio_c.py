n = 0
while n < 1:
    resposta = input('Digite um número positivo: ')
    n = int(resposta)

print('[', end='')

contador = 1
while contador <= n:
    caractere_final = '|'
    if contador == n:
        caractere_final = ''
    print(contador, end=caractere_final)
    contador = contador + 1

print(']')
