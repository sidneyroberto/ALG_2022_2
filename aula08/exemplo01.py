from random import randint

def somar(n1, n2): # assinatura da função
    resultado = n1 + n2
    print('%d + %d = %d' % (n1, n2, resultado))

somar(2, 3)

def sortear_numero_megasena():
    numero = randint(1, 60)
    return numero

numero_sorteado = sortear_numero_megasena()
print('Nro sorteado: %d' % numero_sorteado)