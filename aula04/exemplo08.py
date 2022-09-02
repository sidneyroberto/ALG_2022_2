import re

frase_suja = '   Oi. Isto é uma frase.   '
cpf = '   000. 000.  000 - 00   '

frase_limpa = frase_suja.strip()
print(frase_limpa)

cpf_limpo = cpf.replace(' ', '')
print(cpf_limpo)
cpf_limpo2 = re.sub('[\s\.-]', '', cpf)
print(cpf_limpo2)
