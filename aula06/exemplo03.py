lista1 = [12, 34, 65, 3]
lista2 = [6, -4, 75, 129, 233]
lista1.extend(lista2)
print(lista1)

lista1 = [12, 34, 65, 3]
for numero in lista2:
    lista1.append(numero)

print(lista1)

lista1 = [12, 34, 65, 3]
contador = 0
while contador < len(lista2):
    lista1.append(lista2[contador])
    contador += 1

print(lista1)
