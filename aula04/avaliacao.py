frase = input('Digite uma frase: ')

tamanho = len(frase)
if tamanho % 3 == 0:
    parte = int(tamanho / 3)
    print(frase[0:parte])
    print(frase[parte:parte * 2])
    print(frase[parte * 2:])
else:
    parte = int(tamanho / 2)
    print(frase[0:parte])
    print(frase[parte:])
