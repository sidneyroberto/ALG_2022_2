cores_roupas = {
    'calça': 'azul',
    'meias': 'branco',
    'camiseta': 'verde'
}

if 'blusa' not in cores_roupas:
    cores_roupas['blusa'] = 'amarelo'
print(cores_roupas)

del cores_roupas['meias']
print(cores_roupas)

cores_roupas.clear()
print(cores_roupas)
