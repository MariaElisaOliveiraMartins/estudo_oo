'''
Exemplo de classe que inicializa um objeto com multiplos atributos.
'''


class CadCli ():

    def __init__(self, param_nome, param_idade, param_sexo, param_filhos):

        self.nome = param_nome
        self.idade = param_idade
        self.sexo = param_sexo
        self.filhos = list(param_filhos)

if __name__ == '__main__':
    lista = ['joao', 'josé', 'juca', 'joel']
    print('\nlista = ', type(lista))
    dados_do_cliente = CadCli('Beltrano', 38, None, lista)
    print('\nDados Cadastrais\n')
    print('nome: ', dados_do_cliente.nome)
    print('idade: ', dados_do_cliente.idade)
    print('sexo: ', dados_do_cliente.sexo)
    print('filhos: ')
    for idx, item in enumerate(dados_do_cliente.filhos):
        print(idx + 1, item)
