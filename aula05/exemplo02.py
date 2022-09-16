resposta = input('Digite um número positivo: ')
n = int(resposta)
while n < 1:
    print('O número deve ser positivo!')
    resposta = input('Digite um número positivo: ')
    n = int(resposta)

for contador in range(1, n + 1):
    print(contador, end=' ')
