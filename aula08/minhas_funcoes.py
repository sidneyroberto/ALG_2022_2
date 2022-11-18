def fibonacci(n):
    if n < 1:
        return -1
    
    if n == 1:
        return '0'
    
    if n == 2:
        return '0, 1'
    
    sequencia = '0, 1'
    anterior = 1
    atual = 1
    contador = 3
    while contador <= n:
        sequencia += ', ' + str(atual)
        aux = atual
        atual += anterior
        anterior = aux
        contador += 1
    
    return sequencia

def celsius_para_farenheit(celsius):
    return celsius * 1.8 + 32

def velocidade_media(variacao_espaco, variacao_tempo):
    return variacao_espaco / variacao_tempo
