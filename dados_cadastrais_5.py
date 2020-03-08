'''
Exemplo de definição e utilização de um método de classe (exemplo 2).
'''

class DadosCad ():

    estado_civil = 'solteira'

    def __init__(self, param_nome, param_idade, param_sexo, *param_filho_da_mae):

        self.nome = param_nome
        self.idade = param_idade
        self.sexo = param_sexo
        self.filho = list(param_filho_da_mae)

    @classmethod
    def data_e_hora_atual(cls):

        from datetime import datetime
        data_e_hora = datetime.now()
        return(data_e_hora.strftime('%d/%m/%Y %HH:%MM:%SS'))


def exibe_dados ():
    print('Atributos de Fulana: ', fulana.__dict__)
    print('Atributos de Beltrana:', beltrana.__dict__)
    print('Estado Civil de Fulana: ', fulana.estado_civil, 'id: ', id(fulana.estado_civil))
    print('Estado Civil de Beltrana: ', beltrana.estado_civil, 'id: ', id(beltrana.estado_civil))
    print('Estado Civil da Classe: ', DadosCad.estado_civil, 'id: ', id(DadosCad.estado_civil))


if __name__ == '__main__':

    fulana = DadosCad('Fulana', 38, 'F', 'Beltrana')
    beltrana = DadosCad('Beltrana',18, 'F', None)
    print('\n1) Mostrando o valor e o id do estado_civil em ', DadosCad.data_e_hora_atual(), ': \n')
    exibe_dados()

    print('\n2) Alterado o valor do estado_civil no objeto em ', fulana.data_e_hora_atual(), ' \n :')
    fulana.estado_civil = 'casada'
    exibe_dados()

    print('\n2) Alterado o valor do estado_civil no objeto em ', beltrana.data_e_hora_atual(), ' \n :')
    beltrana.estado_civil = 'divorciada'
    exibe_dados()

