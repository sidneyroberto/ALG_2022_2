from random import randint

def ler_numero_real(mensagem):
    resposta = input(mensagem)
    return float(resposta)

def ler_numero_inteiro(mensagem):
    resposta = input(mensagem)
    return int(resposta)

def calcular_prestacao(valor, tipo_cliente, quantidade_parcelas):
    taxa_juros = definir_taxa_juros(tipo_cliente)
    montante = valor * (1 + (taxa_juros / 100) * quantidade_parcelas)
    return montante / quantidade_parcelas

def definir_taxa_juros(tipo_cliente):
    if tipo_cliente == 'Standard':
        return 2.5
    if tipo_cliente == 'Platinum':
        return 1.99
    if tipo_cliente == 'Gold':
        return 1.2
    
    raise Exception('Tipo de cliente inválido')  

def calcular_sequencia_crescente_decrescente(n):
    sequencia = ''
    if n > 0:
        for i in range(1, n + 1):
            sequencia += str(i)
            if i < n:
                sequencia += ', '
        
        sequencia += ', ' if n > 1 else ''
        for i in reversed(range(1, n)):
            sequencia += str(i)
            if i > 1:
                sequencia += ', '
    
    return sequencia

def contar_quantas_vezes_sete_aparece(lista):
    contador = lista.count(7)
    return contador

def sortear_numeros(quantidade, limite_inferior, limite_superior):
    numeros = []
    
    if quantidade > 0 and limite_inferior < limite_superior:
        for _ in range(quantidade):
            numero = randint(limite_inferior, limite_superior)
            numeros.append(numero)
    
    return numeros