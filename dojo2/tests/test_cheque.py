#coding: utf-8
import unittest2
from cheque import Cheque

class ChequeTestCase(unittest2.TestCase):
    
    def test_escrever_unidade(self):
        
        cheque = Cheque(111)
        
        self.assertEquals(cheque.get_unidade(1), "um")
        self.assertEquals(cheque.get_unidade(2), "dois")
        self.assertEquals(cheque.get_unidade(3), "três")
        self.assertEquals(cheque.get_unidade(4), "quatro")
        self.assertEquals(cheque.get_unidade(5), "cinco")
        self.assertEquals(cheque.get_unidade(6), "seis")
        self.assertEquals(cheque.get_unidade(7), "sete")
        self.assertEquals(cheque.get_unidade(8), "oito")
        self.assertEquals(cheque.get_unidade(9), "nove")
        
    
    def test_escrever_dezenas(self):
        
        cheque = Cheque(111)
        
        self.assertEquals(cheque.get_dezena(10), "dez")
        self.assertEquals(cheque.get_dezena(11), "onze")
        self.assertEquals(cheque.get_dezena(12), "doze")
        self.assertEquals(cheque.get_dezena(13), "treze")
        self.assertEquals(cheque.get_dezena(14), "quatorze")
        self.assertEquals(cheque.get_dezena(15), "quinze")
        self.assertEquals(cheque.get_dezena(16), "dezesseis")
        self.assertEquals(cheque.get_dezena(17), "dezessete")
        self.assertEquals(cheque.get_dezena(18), "dezoito")
        self.assertEquals(cheque.get_dezena(19), "dezenove")
        self.assertEquals(cheque.get_dezena(20), "vinte")
        self.assertEquals(cheque.get_dezena(21), "vinte e um")
        self.assertEquals(cheque.get_dezena(30), "trinta")
        self.assertEquals(cheque.get_dezena(40), "quarenta")
        self.assertEquals(cheque.get_dezena(50), "cinquenta")
        self.assertEquals(cheque.get_dezena(60), "sessenta")
        self.assertEquals(cheque.get_dezena(70), "setenta")
        self.assertEquals(cheque.get_dezena(80), "oitenta")
        self.assertEquals(cheque.get_dezena(90), "noventa")
    
    def test_escrever_centenas(self):
        
        cheque = Cheque(111)
        self.assertEquals(cheque.get_centena(100), "cem")
        self.assertEquals(cheque.get_centena(101), "cento e um")
        self.assertEquals(cheque.get_centena(111), "cento e onze")
        self.assertEquals(cheque.get_centena(200), "duzentos")
        self.assertEquals(cheque.get_centena(220), "duzentos e vinte")
        self.assertEquals(cheque.get_centena(300), "trezentos")
        self.assertEquals(cheque.get_centena(342), "trezentos e quarenta e dois")    
        self.assertEquals(cheque.get_centena(400), "quatrocentos")
        self.assertEquals(cheque.get_centena(500), "quinhentos")
        self.assertEquals(cheque.get_centena(600), "seiscentos")
        self.assertEquals(cheque.get_centena(700), "setecentos")
        self.assertEquals(cheque.get_centena(800), "oitocentos")
        self.assertEquals(cheque.get_centena(900), "novecentos")
        
    def test_escrever_milhar(self):
        cheque = Cheque(111)
        
        self.assertEquals(cheque.get_milhar_por_extenso(1000), "um mil")
        self.assertEquals(cheque.get_milhar_por_extenso(1999), "um mil novecentos e noventa e nove")
        self.assertEquals(cheque.get_milhar_por_extenso(2000), "dois mil")
        self.assertEquals(cheque.get_milhar_por_extenso(1090), "um mil e noventa")
        self.assertEquals(cheque.get_milhar_por_extenso(3008), "três mil e oito")

    def test_escrever_numero_inteiro_maior_que_um(self):
        cheque = Cheque(1234)
        self.assertEquals(cheque.get_valor_por_extenso(), "um mil duzentos e trinta e quatro reais")

        cheque = Cheque(15987)
        self.assertEquals(cheque.get_valor_por_extenso(), "quinze mil novecentos e oitenta e sete reais")

        cheque = Cheque(315987)
        self.assertEquals(cheque.get_valor_por_extenso(), "trezentos e quinze mil novecentos e oitenta e sete reais")

    def test_escrever_um_por_extenso(self):
        cheque = Cheque(1)
        self.assertEquals(cheque.get_valor_por_extenso(), "um real")

    def test_escrever_validate_valor(self):
        
        with self.assertRaises(ValueError):
            cheque = Cheque(-100)
            
    def test_escrever_numero_com_dezena_de_centavo(self):
        cheque = Cheque(111.10)
        self.assertEquals(cheque.get_valor_por_extenso(), "cento e onze reais e dez centavos")

    def test_escrever_numero_com_unidade_de_centavo(self):
        cheque = Cheque(30004.03)
        self.assertEquals(cheque.get_valor_por_extenso(), "trinta mil e quatro reais e três centavos")

    def test_escrever_numero_so_com_centavos(self):
        cheque = Cheque(0.43)
        self.assertEquals(cheque.get_valor_por_extenso(), "quarenta e três centavos")
        
        