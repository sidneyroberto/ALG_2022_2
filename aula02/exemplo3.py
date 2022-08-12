resposta = input('Digite o grau em Farenheit: ')
farenheit = float(resposta)

celsius1 = (farenheit - 32) * (5/9)
celsius2 = (farenheit - 32) / 1.8

print('%f °F = %.0f °C' % (farenheit, celsius1))
print('%f °F = %d °C' % (farenheit, celsius2))
