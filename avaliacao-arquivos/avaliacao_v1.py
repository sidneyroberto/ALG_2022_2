'''
OBS: Esta versão só funciona em diretórios que contém
apenas dois níveis
'''
from os import listdir
from os.path import isdir , join, getsize

caminho_pasta = 'arquivos'
quantidade_por_extensao = {}
quantidade_arquivos = 0
quantidade_subpastas = 0
tamanho_total_megabytes = 0

for arquivo in listdir(caminho_pasta):
    caminho_arquivo = join(caminho_pasta, arquivo)
    if isdir(caminho_arquivo):
        quantidade_subpastas += 1
        for subarquivo in listdir(caminho_arquivo):
            caminho_subarquivo = join(caminho_arquivo, subarquivo)
            tamanho_total_megabytes += getsize(caminho_subarquivo)
            quantidade_arquivos += 1
            partes = subarquivo.split('.')
            extensao = partes[len(partes) - 1].lower()
            if extensao in quantidade_por_extensao:
                quantidade = quantidade_por_extensao[extensao]
                quantidade_por_extensao[extensao] = quantidade + 1
            else:
                quantidade_por_extensao[extensao] = 1
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
print('Quantidade subpastas: %d' % quantidade_subpastas)
tamanho_total_megabytes = tamanho_total_megabytes / 1024 / 1024
print('Tamanho total dos arquivos: %.2f mb' % tamanho_total_megabytes)
print('Quantidade por extensao:')
print(quantidade_por_extensao)