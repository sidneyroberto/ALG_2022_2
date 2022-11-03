'''
linguagens = {}
print(linguagens)
linguagens['TII'] = 'JavaScript'
linguagens['TSI'] = 'TypeScript'
linguagens['TRC'] = 'Python'
'''
linguagens = {
    'TII': 'JavaScript',
    'TSI': 'TypeScript',
    'TRC': 'Python',
}

for chave, valor in linguagens.items():
    print('%s: %s' % (chave, valor))

for chave in linguagens.keys():
    print('%s: %s' % (chave, linguagens[chave]))

for valor in linguagens.values():
    print(valor)

chaves = list(linguagens.keys())
contador = 0
while contador < len(chaves):
    chave = chaves[contador]
    print('%s: %s' % (chave, linguagens[chave]))
    contador += 1
