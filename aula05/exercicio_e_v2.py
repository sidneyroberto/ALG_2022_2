n = 0
while n < 1:
    resposta = input('Digite um número positivo: ')
    n = int(resposta)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        final = ', '
        if j == i:
            final = ''
        print(j, end=final)
    print()

for i in reversed(range(1, n)):
    for j in range(1, i + 1):
        final = ', '
        if j == i:
            final = ''
        print(j, end=final)
    print()
