import unittest2
from poker.carta import Carta
from poker.mao import Mao

class MaoTestCase(unittest2.TestCase):
    
    def test_criar_mao(self):
        
        cartas = [
            Carta(valor=Carta.AS, naipe=Carta.OURO),
            Carta(valor=Carta.DOIS, naipe=Carta.OURO),
            Carta(valor=Carta.TRES, naipe=Carta.OURO),
            Carta(valor=Carta.QUATRO, naipe=Carta.OURO),
            Carta(valor=Carta.CINCO, naipe=Carta.OURO)
        ]
        
        mao = Mao(cartas=cartas)
        
        self.assertEquals(mao.cartas, cartas)
        
    def test_verifica_se_mao_nao_e_royal_flush(self):
        
        cartas = [
            Carta(valor=Carta.AS, naipe=Carta.OURO),
            Carta(valor=Carta.DOIS, naipe=Carta.OURO),
            Carta(valor=Carta.TRES, naipe=Carta.OURO),
            Carta(valor=Carta.QUATRO, naipe=Carta.OURO),
            Carta(valor=Carta.CINCO, naipe=Carta.OURO)
        ]
        
        mao = Mao(cartas = cartas)
        
        self.assertEquals(mao.is_royalflush(), False)
        
    def test_verifica_se_mao_e_royal_flush(self):

        cartas = [
            Carta(valor=Carta.DEZ, naipe=Carta.OURO),
            Carta(valor=Carta.VALETE, naipe=Carta.OURO),
            Carta(valor=Carta.DAMA, naipe=Carta.OURO),
            Carta(valor=Carta.REI, naipe=Carta.OURO),
            Carta(valor=Carta.AS, naipe=Carta.OURO)
        ]

        mao = Mao(cartas = cartas)

        self.assertEquals(mao.is_royalflush(), True)
        
    def test_cartas_estao_ordenadas(self):
        carta_as = Carta(valor=Carta.AS, naipe=Carta.OURO)
        carta_dois = Carta(valor=Carta.DOIS, naipe=Carta.OURO)
        carta_tres = Carta(valor=Carta.TRES, naipe=Carta.OURO)
        carta_quatro = Carta(valor=Carta.QUATRO, naipe=Carta.OURO)
        carta_cinco = Carta(valor=Carta.CINCO, naipe=Carta.OURO)
        
        cartas_desordenadas = [carta_as, carta_dois, carta_quatro, carta_tres, carta_cinco]
        cartas_ordenadas = [carta_as, carta_dois, carta_tres, carta_quatro, carta_cinco]
        
        mao = Mao(cartas = cartas_desordenadas)
        
        self.assertEquals(mao.cartas, cartas_ordenadas)
        
    def test_cartas_estao_ordenadas_verifca_as(self):
        carta_as = Carta(valor=Carta.AS, naipe=Carta.OURO)
        carta_dois = Carta(valor=Carta.DOIS, naipe=Carta.OURO)
        carta_tres = Carta(valor=Carta.DOIS, naipe=Carta.OURO)
        carta_quatro = Carta(valor=Carta.QUATRO, naipe=Carta.OURO)
        carta_cinco = Carta(valor=Carta.CINCO, naipe=Carta.OURO)

        cartas_desordenadas = [carta_as, carta_dois, carta_quatro, carta_tres, carta_cinco]
        cartas_ordenadas = [carta_dois, carta_tres, carta_quatro, carta_cinco, carta_as]

        mao = Mao(cartas = cartas_desordenadas)

        self.assertEquals(mao.cartas, cartas_ordenadas)
        
    def test_verifica_se_mao_e_flush(self):
        cartas = [
            Carta(valor=Carta.QUATRO, naipe=Carta.OURO),
            Carta(valor=Carta.AS, naipe=Carta.OURO),
            Carta(valor=Carta.SEIS, naipe=Carta.OURO),
            Carta(valor=Carta.SETE, naipe=Carta.OURO),
            Carta(valor=Carta.OITO, naipe=Carta.OURO)
        ]

        mao = Mao(cartas = cartas)

        self.assertEquals(mao.is_flush(), True)
        
    def test_verifica_se_mao_nao_e_flush(self):
        cartas = [
            Carta(valor=Carta.QUATRO, naipe=Carta.OURO),
            Carta(valor=Carta.AS, naipe=Carta.OURO),
            Carta(valor=Carta.SEIS, naipe=Carta.PAUS),
            Carta(valor=Carta.SETE, naipe=Carta.OURO),
            Carta(valor=Carta.OITO, naipe=Carta.OURO)
        ]

        mao = Mao(cartas = cartas)

        self.assertEquals(mao.is_flush(), False)
        
    def test_verifica_se_mao_e_straight(self):
        cartas = [
            Carta(valor=Carta.QUATRO, naipe=Carta.OURO),
            Carta(valor=Carta.CINCO, naipe=Carta.OURO),
            Carta(valor=Carta.SEIS, naipe=Carta.PAUS),
            Carta(valor=Carta.SETE, naipe=Carta.OURO),
            Carta(valor=Carta.OITO, naipe=Carta.OURO)
        ]

        mao = Mao(cartas = cartas)

        self.assertEquals(mao.is_straight(), True)
        
    def test_verifica_se_mao_e_o_four(self):
        cartas = [
            Carta(valor=Carta.QUATRO, naipe=Carta.COPAS),
            Carta(valor=Carta.QUATRO, naipe=Carta.ESPADAS),
            Carta(valor=Carta.QUATRO, naipe=Carta.PAUS),
            Carta(valor=Carta.QUATRO, naipe=Carta.OURO),
            Carta(valor=Carta.OITO, naipe=Carta.OURO)
        ]

        mao = Mao(cartas = cartas)

        self.assertEquals(mao.is_four(), True)