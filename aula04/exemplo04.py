frase = 'abacaxi'
print(frase[0::])
print(frase[3::])
print(frase[1:6:2])
print(frase[::2])

tamanho = len(frase)
metade = int(tamanho / 2)
primeira_metade = frase[:metade]
segunda_metade = frase[metade:]
print(primeira_metade)
print(segunda_metade)
