resposta = input('Digite o valor do empréstimo: ')
valor = float(resposta)
resposta = input('Digite a taxa de juros: ')
taxa = float(resposta)
resposta = input('Digite a quantidade de parcelas: ')
parcelas = int(resposta)

montante = valor * (1 + (taxa / 100) * parcelas)
prestacao = montante / parcelas

print('Montante a ser pago: %.2f' % montante)
print('Valor da prestação: %.2f' % prestacao)
