# Inicializa a lista com uma lista vazia
elementos = []

# Inserção de novos elementos
elementos.append(5)
print(elementos)
elementos.append('Sidney')
elementos.append(True)
print(elementos)
elementos.insert(0, 'Início')
print(elementos)

# Remoção de elementos
elementos.remove('Início')
print(elementos)
elementos.pop()
print(elementos)
elementos.pop(0)
print(elementos)
