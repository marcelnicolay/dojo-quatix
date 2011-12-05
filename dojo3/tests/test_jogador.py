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
        
    def test_get_tabuleiro(self):

        jogador = Jogador()
        
        embarcacao1 = PortaAvioes(posicao=(5,0), is_horizontal=True)
        embarcacao2 = Submarino(posicao=(3,5), is_horizontal=False)
        
        jogador.adicionar_embarcacao(embarcacao1)
        jogador.adicionar_embarcacao(embarcacao2)
        
        a = Jogador.AGUA
        e = Jogador.EMBARCACAO
        
        tabuleiro = [
            [a, a, a, a, a, e, e, e, e, e],
            [a, a, a, a, a, a, a, a, a, a],
            [a, a, a, a, a, a, a, a, a, a],
            [a, a, a, a, a, a, a, a, a, a],
            [a, a, a, a, a, a, a, a, a, a],
            [a, a, a, e, a, a, a, a, a, a],
            [a, a, a, e, a, a, a, a, a, a],
            [a, a, a, e, a, a, a, a, a, a],
            [a, a, a, a, a, a, a, a, a, a],
            [a, a, a, a, a, a, a, a, a, a],
        ]
        
        self.assertEquals(jogador.get_tabuleiro(), tabuleiro)
        
    def test_get_tabuleiro_atirado(self):
        
        jogador = Jogador()
        
        embarcacao1 = PortaAvioes(posicao=(5,0), is_horizontal=True)
        embarcacao2 = Submarino(posicao=(3,5), is_horizontal=False)
        
        jogador.adicionar_embarcacao(embarcacao1)
        jogador.adicionar_embarcacao(embarcacao2)
        
        jogador.atirar((3,5))
        jogador.atirar((5,0))
        jogador.atirar((2,0))
        
        a = Jogador.AGUA
        e = Jogador.EMBARCACAO
        ta = Jogador.TIRO_AGUA
        te = Jogador.TIRO_EMBARCACAO
        
        tabuleiro = [
            [a, a, ta, a, a, te, e, e, e, e],
            [a, a, a, a, a, a, a, a, a, a],
            [a, a, a, a, a, a, a, a, a, a],
            [a, a, a, a, a, a, a, a, a, a],
            [a, a, a, a, a, a, a, a, a, a],
            [a, a, a, te, a, a, a, a, a, a],
            [a, a, a, e, a, a, a, a, a, a],
            [a, a, a, e, a, a, a, a, a, a],
            [a, a, a, a, a, a, a, a, a, a],
            [a, a, a, a, a, a, a, a, a, a],
        ]
        
        self.assertEquals(jogador.get_tabuleiro(), tabuleiro)
        
    def test_todas_embarcacoes_afundadas(self):
        
        jogador = Jogador()
        jogador.adicionar_embarcacao(PortaAvioes(posicao=(5,0), is_horizontal=True))

        self.assertFalse(jogador.is_terminado())
        
        jogador.atirar((5,0))
        jogador.atirar((6,0))
        jogador.atirar((7,0))
        jogador.atirar((8,0))
        jogador.atirar((9,0))
        
        self.assertTrue(jogador.is_terminado())
        