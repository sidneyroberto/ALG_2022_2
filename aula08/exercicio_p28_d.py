'''
Página 28, exercício d (criar uma função para calcular
e retornar a sequência)
'''
import funcoes_exercicios as fe

n = fe.ler_numero_inteiro('Digite o tamanho da sequência: ')
sequencia = fe.calcular_sequencia_crescente_decrescente(n)
print(sequencia)