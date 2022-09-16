n = 0
while n < 1:
    resposta = input('Digite um número positivo: ')
    n = int(resposta)

contador1 = 1
while contador1 <= n:
    contador2 = 1
    while contador2 <= contador1:
        final = ', '
        if contador2 == contador1:
            final = ''
        print(contador2, end=final)
        contador2 = contador2 + 1
    print()
    contador1 = contador1 + 1


contador1 = n - 1
while contador1 >= 1:
    contador2 = 1
    while contador2 <= contador1:
        final = ', '
        if contador2 == contador1:
            final = ''
        print(contador2, end=final)
        contador2 = contador2 + 1
    print()
    contador1 = contador1 - 1
