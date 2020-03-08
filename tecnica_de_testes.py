'''
Exemplo sobre como utilizar a biblioteca de teste do Python para testar códigos escritos em Python.
'''

from unittest import TestCase

from Estudo_OO.dirigindo_um_carro_3 import Motor

class TestaMotorCarro (TestCase):


    def test_velocidade_atual (self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade_atual)


    def test_aceleracao (self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade_atual)
        motor.acelerar()
        self.assertEqual(2, motor.velocidade_atual)
