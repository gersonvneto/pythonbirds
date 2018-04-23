from unittest import TestCase
from oo.carro import Motor

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):   # herdar da test case e comecar o teste com o prefixo test
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)












