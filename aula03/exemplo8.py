resposta = input('Digite a nota b1: ')
nota_b1 = float(resposta)

resposta = input('Digite a nota b2: ')
nota_b2 = float(resposta)

media = (nota_b1 + nota_b2) / 2

situacao = 'aprovado' if media >= 6 else 'reprovado'

print('O estudante foi %s com média %.1f' % (situacao, media))
