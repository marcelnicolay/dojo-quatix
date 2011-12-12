import unittest2
from poker.carta import Carta

class CartaTestCase(unittest2.TestCase):
    
    def test_criar_carta(self):
        carta = Carta(valor=Carta.DOIS, naipe=Carta.COPAS)
        
        self.assertEquals(carta.valor,Carta.DOIS)
        self.assertEquals(carta.naipe,Carta.COPAS)
        
    def test_criar_carta_invalida(self):
        with self.assertRaises(ValueError):
            carta = Carta(valor=50, naipe=23)
        