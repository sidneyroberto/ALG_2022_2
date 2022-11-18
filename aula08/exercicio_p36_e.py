'''
Página 36, exercício e (criar uma função para realizar
os sorteios e retornar os números sorteados e outra função
para retornar a quantidade de vezes que o número 7 aparece
na sequência de números sorteados)
'''
import funcoes_exercicios as fe

numeros = fe.sortear_numeros(20, 1, 10)
quantidade_vezes_sete_aparece = fe.contar_quantas_vezes_sete_aparece(numeros)

print('Valores sorteados:', end=' ')
print(numeros)
print('Quantidade de vezes que 7 aparece: %d' % quantidade_vezes_sete_aparece)