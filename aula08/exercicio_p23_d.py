'''
Página 23, exercício d (criar função para calcular e retornar
o valor da parcela)
'''

import funcoes_exercicios as fe

valor = fe.ler_numero_real('Digite o valor do empréstimo: ')
tipo_cliente = input('Qual o tipo de cliente: ')
quantidade_parcelas = fe.ler_numero_inteiro('Digite a quantidade de parcelas: ')

valor_parcela = fe.calcular_prestacao(valor, tipo_cliente, quantidade_parcelas)
print('Valor da parcela: %.2f' % valor_parcela)