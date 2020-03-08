'''
Exemplo de Herança Simples onde a classe CadFunc herda todos os métodos e atributos da classe DadosCad.
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


class CadFunc (DadosCad):
    pass


def exibe_dados (pessoa):
    print('\n --- Cadastro ---- \n')
    print('Nome Cadastrado : ', pessoa.nome)
    print('Idade : ', pessoa.idade)
    print('Sexo : ', pessoa.sexo)
    print('Estado Civil : ', pessoa.estado_civil)
    if pessoa.filho != None:
        print('Filhos : ', pessoa.filho)


if __name__ == '__main__':

    fulana = DadosCad('Fulana', 38, 'F', 'Beltrana')
    exibe_dados(fulana)
    beltrana = DadosCad('Beltrana',18, 'F', None)
    exibe_dados(beltrana)
    sicrana = CadFunc('Sicrina', 58, 'F', 'fulana')
    exibe_dados(sicrana)
