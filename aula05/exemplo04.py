n = 0
while n < 1:
    resposta = input('Digite um número positivo: ')
    n = int(resposta)

soma = 0
i = 1
while i <= n:
    soma = soma + i
    i = i + 1

print('Somatório de %d: %d' % (n, soma))

number = 1E-10
