frase = input('Digite uma frase: ')

contador = 0
vogais = 'aeiou'
for caractere in frase.lower():
    if caractere in vogais:
        contador += 1

print('A sua frase contém %d ocorrências de vogais' % contador)
