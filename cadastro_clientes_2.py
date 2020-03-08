'''
Exemplo de classes que utilizam inicializam um objeto com atributo de dados de 3 formas
diferentes: atribuindo vazio, uma constante e um valor variável, respectivamente.
'''

class InicNome_1 ():

    def __init__(self):
        self.atrib = None


class InicNome_2 ():

    def __init__(self):
        self.atrib = 'Fulano'


class InicNome_3 ():

    def __init__(self, param):
        self.atrib = param


if __name__ == '__main__':

    nome = InicNome_1()
    print('\n Inicializando objeto sem conteúdo (atributo vazio): nome.atrib =', nome.atrib)

    nome = InicNome_2()
    print('\n Inicializando objeto com conteúdo (atributo constante): nome.atrib =', nome.atrib)

    nome = InicNome_3('Sicrano')
    print('\n Inicializando objeto com conteúdo (atributo variável): nome.atrib =', nome.atrib)
