frase1 = 'XXXXXXXXXX'
frase2 = 'YYYYYYYYYY'

resultado = frase1 + frase2
print(resultado)

'''
    Altere o resultado acima para que ele receba
    a intercalação entre as duas frases:
    
    XYXYXYXYXYXYXYXYXYXY
'''
resultado = resultado[::10] * 10
print(resultado)
