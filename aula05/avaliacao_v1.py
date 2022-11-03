n = 0
while n < 1:
    resposta = input('Digite a quantidade de elementos (ao menos 1): ')
    n = int(resposta)

r = 0
while r < 1:
    resposta = input('Digite a razão entre os elementos (ao menos 1): ')
    r = int(resposta)

elemento = 1

for i in range(1, n + 1):
    caractere_final = ', ' if i < n else ''
    print(elemento, end=caractere_final)
    elemento += r
