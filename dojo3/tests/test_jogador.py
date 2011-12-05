import unittest2
from batalha.jogador import Jogador
from batalha.embarcacao import *

class JogadorTestCase(unittest2.TestCase):

    def test_adicionar_peca(self):
        jogador = Jogador()
        porta_avioes = PortaAvioes(posicao=[0,0], is_horizontal=True)
        
        jogador.adicionar_embarcacao(embarcacao=porta_avioes)
        
    def test_adicionar_peca_fora_tabuleiro(self):
        jogador = Jogador()
        porta_avioes = PortaAvioes(posicao=[9,9], is_horizontal=True)
        
        with self.assertRaises(ValueError):
            jogador.adicionar_embarcacao(embarcacao=porta_avioes)
            
    def test_adicionar_peca_com_colisao(self):
        jogador = Jogador()
        porta_avioes = PortaAvioes(posicao=(0,0), is_horizontal=True)
        submarino = Submarino(posicao=(0,0), is_horizontal=True)
        
        jogador.adicionar_embarcacao(porta_avioes)
        
        with self.assertRaises(ValueError):
            jogador.adicionar_embarcacao(submarino)
            
    def test_tentar_acertar_embarcacao(self):
        jogador = Jogador()
        porta_avioes = PortaAvioes(posicao=(0,0), is_horizontal=True)
        submarino = Submarino(posicao=(2,2), is_horizontal=False)
        
        jogador.adicionar_embarcacao(porta_avioes)
        jogador.adicionar_embarcacao(submarino)
        
        embarcacao_acertada = jogador.atirar((2,4))
        self.assertEqual(embarcacao_acertada, submarino)
        
    def test_atirar_duas_vezes_no_mesmo_lugar(self):
        jogador = Jogador()

        jogador.atirar((2,4))
        jogador.atirar((0,0))
        
        with self.assertRaises(ValueError):            
            jogador.atirar((2,4))

    def test_afundar_embarcacao(self):
        jogador = Jogador()

        porta_avioes = PortaAvioes(posicao=(0,0), is_horizontal=True)
        submarino = Submarino(posicao=(2,2), is_horizontal=False)
        
        jogador.adicionar_embarcacao(porta_avioes)
        jogador.adicionar_embarcacao(submarino)

        jogador.atirar((2,2))
        jogador.atirar((2,3))
        submarino = jogador.atirar((2,4))
        
        self.assertTrue(submarino.afundado)
        
        