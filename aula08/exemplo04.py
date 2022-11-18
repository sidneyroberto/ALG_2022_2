def usa_sapato(**roupas):
    if 'sapato' in roupas:
        return True
    
    return False

usa = usa_sapato(meia = 'branca', sapato = 'azul', calca = 'bege')
print(usa)
'''
roupas['meia'] = 'branca'
roupas['sapato'] = 'azul'
roupas['calca'] = 'bege'
'''

def imprimir_ficha_estudante(**ficha):
    print('Nome: %s' % ficha['nome'])
    print('CPF: %s' % ficha['cpf'])
    print('RA: %s' % ficha['ra'])
    print('E-mail: %s' % ficha['email'])
    print('Endereço: %s' % ficha['endereco'])
    
imprimir_ficha_estudante(
    nome = 'João da Silva',
    ra = '51232',
    email = 'jao@email.com',
    endereco = 'Rua 7 de setembro, 22',
    cpf = '999.999.999-99'
)