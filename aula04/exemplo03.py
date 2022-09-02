#frase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
frase = input('Digite uma frase: ')
tamanho = len(frase)
print(tamanho)
metade = int(tamanho / 2)
primeira_metade = frase[0:metade]
segunda_metade = frase[metade:tamanho]
print(primeira_metade)
print(segunda_metade)

#primeira_metade = frase[-26:-13]
#segunda_metade = frase[-13:tamanho]
primeira_metade = frase[-tamanho:-metade]
segunda_metade = frase[-metade:tamanho]
print(primeira_metade)
print(segunda_metade)
