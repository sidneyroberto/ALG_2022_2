import minhas_funcoes as mf
# from minhas_funcoes import fibonacci

sequencia = mf.fibonacci(5)
# sequencia = fibonacci(10)
print(sequencia)

conteudo = dir(mf)
print(conteudo)

farenheit = mf.celsius_para_farenheit(25)
print('%f F' % farenheit)

velocidade_media = mf.velocidade_media(10, 2)
print('%f km/h' % velocidade_media)