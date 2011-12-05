import unittest2
from batalha.embarcacao import *

class EmbarcacaoTestCase(unittest2.TestCase):
    
    def test_criar_embarcacao(self):
        
        embarcacao = Embarcacao(tamanho=5, posicao=[0,0], is_horizontal=True)
        
    def test_criar_embarcacao_invalida(self):

        with self.assertRaises(ValueError):
            embarcacao = Embarcacao(tamanho=6, posicao=[0,0], is_horizontal=True)

        with self.assertRaises(ValueError):
            embarcacao = Embarcacao(tamanho=1, posicao=[0,0], is_horizontal=True)

    def test_get_posicoes(self):
        embarcacao = Embarcacao(tamanho=5, posicao=[0,1], is_horizontal=False)
        expected = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
        posicoes = embarcacao.get_posicoes()
        self.assertEqual(expected, posicoes)

class PortaAvioesTestCase(unittest2.TestCase):
    def test_criar_portaavioes(self):
        porta_avioes = PortaAvioes(posicao=[0,0], is_horizontal=True)
        self.assertEqual(porta_avioes.tamanho, 5)
     
class EncouracadoTestCase(unittest2.TestCase):
    def test_criar_encouracado(self):
        encouracado = Encouracado(posicao=[0,0], is_horizontal=True)
        self.assertEqual(encouracado.tamanho, 4)
        
class SubmarinoTestCase(unittest2.TestCase):
    def test_criar_submarino(self):
        submarino = Submarino(posicao=[0,0], is_horizontal=True)
        self.assertEqual(submarino.tamanho, 3)
        
class DestroyerTestCase(unittest2.TestCase):
    def test_criar_destroyer(self):
        destroyer = Destroyer(posicao=[0,0], is_horizontal=True)
        self.assertEqual(destroyer.tamanho, 3)
        
class PatrulhaTestCase(unittest2.TestCase):
    def test_criar_patrulha(self):
        patrulha = Patrulha(posicao=[0,0], is_horizontal=True)
        self.assertEqual(patrulha.tamanho, 2)