def calcular_delta(a, b, c):
    return b ** 2 - 4 * a * c

# keywords parameters/arguments
delta = calcular_delta(b = 2, a = 1, c = 3)
print(delta)
delta = calcular_delta(1, 2, 3)
print(delta)

# valor default para parâmetro
def imprimir_saudacao(nome = 'Fulano'):
    print('Olá, %s! Tudo bem contigo?' % nome)

imprimir_saudacao('Sidney')
imprimir_saudacao()