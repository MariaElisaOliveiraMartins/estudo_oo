"""
Implemetação da Classe Carro contendo:
1) Classe Motor (acelera ou freia o carro)
2) Classe Direção (vira o carro à direita ou à esquerda)
"""

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Carro():


    class Motor():
        def __init__(self):
            self.velocidade_atual = 0


        def acelerar(self,velocidade):
            self.velocidade_atual = velocidade + 1

        def frear(self,velocidade):
            self.velocidade_atual = velocidade - 2


    class Direcao():

        direita = {NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE}
        esquerda = {NORTE:OESTE, OESTE:SUL, SUL:LESTE, LESTE:NORTE}

        def __init__(self):
            self.direcao_atual = NORTE


        def virar_a_direita(self):
            self.direcao_atual = self.direita[self.direcao_atual]


        def virar_a_esquerda(self):
            self.direcao_atual = self.esquerda[self.direcao_atual]

if __name__ == '__main__':

    ''' Saindo da garangem'''

    carro = Carro().Direcao()

    print('\nVirando à direta 3 vezes:\n')
    for i in list(range(12)):
        carro.virar_a_direita()
        print('seguindo para o ', carro.direcao_atual)

    print('\nVirando à esquerda 3 vezes:\n')
    for i in list(range(12)):
        carro.virar_a_esquerda()
        print('seguindo para o ', carro.direcao_atual)

    print('\nUFA, Estou tonto!\n')

    carro = Carro.Motor()

    ''' Acelerando como louco'''
    for i in list(range(10)):
        carro.acelerar(carro.velocidade_atual)
        print('acelera = ', carro.velocidade_atual)

    '''Freando no susto'''
    for j in list(range(5)):
        carro.frear(carro.velocidade_atual)
        if carro.velocidade_atual <= 0:
            print('PARA! = ', carro.velocidade_atual)
            print ('\nParei! UFA!!!\n')
        else:
            print('PARA! = ', carro.velocidade_atual)

