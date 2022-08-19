resposta = input('Digite o valor a ser emprestado: ')
valor = float(resposta)
resposta = input('Digite o valor da taxa de juros: ')
taxa_juros = float(resposta)
resposta = input('Digite a quantidade de parcelas: ')
parcelas = int(resposta)

montante = valor * (1 + (taxa_juros / 100) * parcelas)
valor_prestacao = montante / parcelas

print('Valor final do empréstimo: %.2f' % montante)
print('Valor de cada prestação: %.2f' % valor_prestacao)
