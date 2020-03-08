'''
Exemplo de utilização e alteração de atributos de classe.
'''

class DadosCad ():

    estado_civil = 'solteira'

    def __init__(self, param_nome, param_idade, param_sexo, *param_filho_da_mae):

        self.nome = param_nome
        self.idade = param_idade
        self.sexo = param_sexo
        self.filho = list(param_filho_da_mae)

def exibe_dados ():
    print('Atributos de Fulana: ', fulana.__dict__)
    print('Atributos de Beltrana:', beltrana.__dict__)
    print('Estado Civil de Fulana: ', fulana.estado_civil, 'id: ', id(fulana.estado_civil))
    print('Estado Civil de Beltrana: ', beltrana.estado_civil, 'id: ', id(beltrana.estado_civil))
    print('Estado Civil da Classe: ', DadosCad.estado_civil, 'id: ', id(DadosCad.estado_civil))


if __name__ == '__main__':

    print('\n1) Mostrando o valor e o id do estado_civil : \n')
    fulana = DadosCad('Fulana', 38, 'F', 'Beltrana')
    beltrana = DadosCad('Beltrana',18, 'F', None)
    exibe_dados()

    print('\n2) Alterado o valor do estado_civil no objeto :')
    fulana.estado_civil = 'casada'
    exibe_dados()

    print('\n3) Alterando o valor do estado_civil na classe :')
    DadosCad.estado_civil = 'divorciada'
    exibe_dados()

    print('\n4) Removendo o atributo estado_civil no objeto :')
    del fulana.estado_civil
    exibe_dados()

