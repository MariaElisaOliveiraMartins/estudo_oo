'''
Exemplo de classe que inicializa um objeto com atributos complexos, isso é,
atributos do mesmo tipo da classe.
'''


class DadosCad ():

    def __init__(self, param_nome, param_idade, param_sexo, *param_filho_da_mae):

        self.nome = param_nome
        self.idade = param_idade
        self.sexo = param_sexo
        self.filho = list(param_filho_da_mae)

def exibe_dados(p_nome, p_idade, p_sexo, p_filho):
    print('nome: ', p_nome)
    print('idade: ', p_idade)
    print('sexo: ', p_sexo)
    print('filhos: ', p_filho)

if __name__ == '__main__':

    beltrana = DadosCad('Beltrana', 18, 'F', None)
    fulana = DadosCad('Fulana', 38, 'F', 'Beltrana')

    print('\nDados Cadastrais de Fulana:\n')
    exibe_dados(fulana.nome, fulana.idade, fulana.sexo, fulana.filho)

    print('\nDados Cadastrais de Bletrana:\n')
    exibe_dados(beltrana.nome, beltrana.idade, beltrana.sexo, beltrana.filho)

