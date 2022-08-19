resposta = input('Digite a nota b1: ')
nota_b1 = float(resposta)

resposta = input('Digite a nota b2: ')
nota_b2 = float(resposta)

media = (nota_b1 + nota_b2) / 2

if media >= 6:
    print('O estudante foi aprovado com média %.1f' % media)
else:
    print('O estudante foi reprovado com média %.1f' % media)
