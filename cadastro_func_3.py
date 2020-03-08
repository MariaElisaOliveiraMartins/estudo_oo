'''
Exemplo de sobreescrita de método onde a classe filha (CadFunc) reutiliza o método da
classe mãe (DadosCad) através do método "super()" e acrescenta mais informações
tornando-se mais especializada.
'''

class DadosCad ():

    estado_civil = 'solteira'

    def __init__(self, param_data_cad, param_nome, param_idade, param_sexo, *param_filho_da_mae):

        self.nome = param_nome
        self.idade = param_idade
        self.sexo = param_sexo
        self.filho = list(param_filho_da_mae)
        self.data_cad = param_data_cad

    def exibe_dados(self):

        print('Nome Cadastrado : ', self.nome)
        print('Idade : ', self.idade)
        print('Sexo : ', self.sexo)
        print('Estado Civil : ', self.estado_civil)
        if self.filho != None:
            print('Filhos : ', self.filho)


    @classmethod
    def data_e_hora_atual(cls):

        from datetime import datetime
        data_e_hora = datetime.now()
        return(data_e_hora.strftime('%d/%m/%Y %HH:%MM:%SS'))


class CadFunc (DadosCad):

    estado_civil = 'divorciada'

    def exibe_dados(self):
        print('\n --- Casdastramento realizado em : ', self.data_cad, ' ---- \n')
        exibe_dados_da_classe_pai = super().exibe_dados()
        print('\n')


if __name__ == '__main__':


    data_cad = CadFunc.data_e_hora_atual()
    fulana = CadFunc(data_cad, 'Fulana', 38, 'F', 'Beltrana' )
    CadFunc.exibe_dados(fulana)
    beltrana = CadFunc(data_cad, 'Beltrana',18, ' F', None)
    beltrana.estado_civil = 'Casada'
    CadFunc.exibe_dados(beltrana)
    sicrana = CadFunc(data_cad, 'Sicrina', 58, 'F', 'fulana')
    CadFunc.exibe_dados(sicrana)



