import re

frase = 'Ontem eu vi 3 animais selvagens'

resultado = frase.upper()
resultado = resultado.replace('A', '_')
resultado = resultado.replace('E', '_')
resultado = resultado.replace('I', '_')
resultado = resultado.replace('O', '_')
resultado = resultado.replace('U', '_')
print(resultado)

frase_maiuscula = frase.upper()
resultado2 = re.sub('[AEIOU]', '_', frase_maiuscula)
print(resultado2)
