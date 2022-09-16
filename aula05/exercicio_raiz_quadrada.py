resposta = input('Digite um número: ')
n = float(resposta)

z = n / 2
y = 0
while abs(z - y) > 1E-10:
    y = z
    z -= (z ** 2 - n) / (2 * z)

print('Raíz quadrada de %f: %f' % (n, z))
