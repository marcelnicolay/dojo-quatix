import unittest2

from batalha.jogo import Jogo
from batalha.jogador import Jogador
from batalha.embarcacao import *

class JogoTestCase(unittest2.TestCase):
    
    def test_criar_jogo(self):
        
        jogo = Jogo()
        jogo.create_jogo()
        
        self.assertEquals(len(jogo.jogadores), 2)
        
        self.assertEquals(len(jogo.jogadores[0].embarcacoes), 5)
        self.assertEquals(len(jogo.jogadores[1].embarcacoes), 5)
                
        
        for embarcacao in (PortaAvioes, Encouracado, Submarino, Destroyer, Patrulha):
            self.assertIn(embarcacao, [e.__class__ for e in jogo.jogadores[0].embarcacoes])
            self.assertIn(embarcacao, [e.__class__ for e in jogo.jogadores[1].embarcacoes])
            
    def test_status_jogo(self):
        
        jogo = Jogo()        
        
        jogador1 = Jogador()
        jogador1.adicionar_embarcacao(Submarino(is_horizontal=True, posicao=(0,0)))
        
        jogador2 = Jogador()
        jogador2.adicionar_embarcacao(Submarino(is_horizontal=True, posicao=(0,0)))
        
        jogo.jogadores.append(jogador1)
        jogo.jogadores.append(jogador2)

        self.assertFalse(jogo.is_terminado())
        
        jogador1.atirar((0,0))
        jogador1.atirar((1,0))
        jogador1.atirar((2,0))
        
        self.assertTrue(jogo.is_terminado())