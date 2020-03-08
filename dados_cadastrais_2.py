'''
Exemplo de criação e remoção dinâmica de atributos a um objeto.
'''


class DadosCad ():

    def __init__(self, param_nome, param_idade, param_sexo, *param_filho_da_mae):

        self.nome = param_nome
        self.idade = param_idade
        self.sexo = param_sexo
        self.filho = list(param_filho_da_mae)

if __name__ == '__main__':

    fulana = DadosCad('Fulana', 38, 'F', 'Beltrana')

    print('\nLista de Atributos de Fulana antes da atribuição e a remoção do atributos : \n')
    print(fulana.__dict__)

    '''criação dinâmica do atributo "sobrenome" '''
    fulana.sobrenome = 'de Tal'

    '''remoção dinâmica do atributo "filho" '''
    del fulana.filho

    print('\nLista de Atributos de Fulana após a atribuição e a remoção do atributos : \n')
    print(fulana.__dict__)


