'''
OBS: Esta versão funciona em diretórios com
2 ou mais níveis
'''
from os import listdir
from os.path import isdir , join, getsize

pastas = ['arquivos']
quantidade_por_extensao = {}
quantidade_arquivos = 0
tamanho_total_megabytes = 0

for pasta in pastas:
    for arquivo in listdir(pasta):
        caminho_arquivo = join(pasta, arquivo)
        if isdir(caminho_arquivo):
            pastas.append(caminho_arquivo)
        else:
            quantidade_arquivos += 1
            tamanho_total_megabytes += getsize(caminho_arquivo)
            partes = arquivo.split('.')
            extensao = partes[len(partes) - 1].lower()
            if extensao in quantidade_por_extensao:
                quantidade = quantidade_por_extensao[extensao]
                quantidade_por_extensao[extensao] = quantidade + 1
            else:
                quantidade_por_extensao[extensao] = 1

print('Quantidade arquivos: %d' % quantidade_arquivos)
print('Quantidade subpastas: %d' % (len(pastas) - 1))
tamanho_total_megabytes = tamanho_total_megabytes / 1024 / 1024
print('Tamanho total dos arquivos: %.2f mb' % tamanho_total_megabytes)
print('Quantidade por extensao:')
print(quantidade_por_extensao)