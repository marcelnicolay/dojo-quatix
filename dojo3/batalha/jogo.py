from batalha.jogador import Jogador
from batalha.embarcacao import *

import random 

class Jogo(object):
    
    def __init__(self):
        self.jogadores = []
    
    def create_jogo(self):
        self.jogadores.append(self.create_jogador())
        self.jogadores.append(self.create_jogador())
    
    def create_jogador(self):
        jogador = Jogador()
        
        embarcacoes = (PortaAvioes, Encouracado, Submarino, Destroyer, Patrulha)

        for embarcacao_class in embarcacoes:
            
            adicionado = False
            while not adicionado:
                
                try:
                    
                    posicao = (random.randint(0,9), random.randint(0,9))
                    embarcacao = embarcacao_class(posicao=posicao, is_horizontal=(random.choice([True,False])))
                    
                    jogador.adicionar_embarcacao(embarcacao)
                    
                    adicionado = True
                except ValueError:
                    continue
            
        return jogador
        
    def is_terminado(self):
        
        for jogador in self.jogadores:
            if jogador.is_terminado():
                return True
                
        return False