resposta = input('Digite a nota b1: ')
nota_b1 = float(resposta)

resposta = input('Digite a nota b2: ')
nota_b2 = float(resposta)

media = (nota_b1 + nota_b2) / 2

if media >= 6:
    print('Estudante aprovado com média %.1f' % media)
elif nota_b1 >= 2 or nota_b2 >= 2:
    print('Estudante de PS com média %.1f' % media)
else:
    print('Estudante reprovado com média %.1f' % media)
