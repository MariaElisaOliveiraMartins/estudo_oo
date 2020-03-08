"""
Implemetação de Colaboração através da Classe Carro, a qual utiliza duas outras classes:
1) Classe Motor (acelera ou freia o carro)
2) Classe Direção (vira o carro à direita ou à esquerda)
"""

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Motor():

    def __init__(self):
        self.velocidade_atual = 0


    def acelerar(self):
        self.velocidade_atual += 1


    def frear(self):
        self.velocidade_atual -= 2



class Direcao():

    prox_a_direita = {NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE}
    prox_a_esquerda = {NORTE:OESTE, OESTE:SUL, SUL:LESTE, LESTE:NORTE}

    def __init__(self):
        self.direcao_atual = NORTE


    def virar_a_direita(self):
        '''print('>>>',self.direcao_atual)'''
        self.direcao_atual = self.prox_a_direita[self.direcao_atual]


    def virar_a_esquerda(self):
        self.direcao_atual = self.prox_a_esquerda[self.direcao_atual]


'''
Implementação da Composiçao (Classe Carro):
Obs: para cada função definida nas classes mais básicas, onde se implementa os 
detalhes dos atributos e das ações que os objetos devem conter e/ou executar,
cria-se uma função para acioná-las através de um "return". 
'''


class Carro():

    def __init__(self, p_motor, p_direcao):
        self.motor = p_motor
        self.direcao = p_direcao


    def velocidade(self):
        return self.motor.velocidade_atual

    def acelerador(self):
        return self.motor.acelerar()

    def freio(self):
        return self.motor.frear()

    def partida(self):
        return self.direcao.direcao_atual

    def direita(self):
        return self.direcao.virar_a_direita()

    def esquerda(self):
        return self.direcao.virar_a_esquerda()


if __name__ == '__main__':

    ''' Saindo da garangem'''

    obj_motor = Motor()
    obj_direcao = Direcao()

    carro = Carro(obj_motor,obj_direcao)
    print('\nInicio : ', carro.partida())

    print('\nAndando em circulos virando à direta (3 voltas):\n')
    for i in list(range(12)):
        carro.direita()
        print('dirigindo o carro para o ', obj_direcao.direcao_atual)

    print('\nAndando em circulos virando à esquerda (3 voltas):\n')
    for i in list(range(12)):
        carro.esquerda()
        print('dirigindo o carro para o ', obj_direcao.direcao_atual)

    print('\nUFA, Estou tonto!\n')

    ''' Acelerando como louco'''

    print('Acelerando:')
    for i in list(range(10)):
        carro.acelerador()
        print('acelera = ', obj_motor.velocidade_atual)

    '''Freando no susto'''

    print('CUIDADO!!!')
    for j in list(range(5)):
        carro.freio()
        if obj_motor.velocidade_atual <= 0:
            print('PARA! = ', obj_motor.velocidade_atual)
            print ('\nParei! UFA!!!\n')
        else:
            print('PARA! = ', obj_motor.velocidade_atual)
