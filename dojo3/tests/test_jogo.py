import unittest2
from batalha.jogo import Jogo

class JogoTestCase(unittest2.TestCase):
    
    def test_criar_jogo(self):
        
        jogo = Jogo()