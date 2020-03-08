'''
Exemplo de uma classe com método cujo objeto é capturado pelo parâmetro "self" da função utilizada por ele,
a qual exibe o id do objeto. O id do objeto também é exibido fora da classe, para que se verifique que se
trata do mesmo objeto.
'''

class CadastroClientes ():
    def nome_cliente(self):
        print('Id do objeto na função: ',id(self))
        return 'Fulano de Tal'

if __name__ == '__main__':
    nome = CadastroClientes()

    '''passagem de parâmetro explícita'''
    print('1) Retorno da função: ', CadastroClientes.nome_cliente(nome), 'Id do Objeto: ', id(nome))
    '''passagem de parâmetro implícita'''
print('2) Retorno da função: ', nome.nome_cliente(), 'Id do Objeto: ', id(nome))

