def somar_v1(numeros):
    somatorio = 0
    
    for n in numeros:
        somatorio += n
    
    return somatorio

# A função recebe argumentos/parâmetros arbitrários
def somar_v2(*numeros):
    somatorio = 0
    
    for n in numeros:
        somatorio += n
    
    return somatorio

lista = [1, 2, 3, 4, 5]
resultado = somar_v1(lista)
print(resultado)

resultado = somar_v2(34, 54, 10)
print(resultado)