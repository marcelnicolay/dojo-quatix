from __future__ import print_function
from batalha.jogo import Jogo
from batalha.jogador import Jogador

import random

def main():
    jogo = Jogo()
    jogo.create_jogo()
    
    print_jogo(jogo)
    
    while not jogo.is_terminado():
        key = raw_input()
        
        print("Jogada "+str(len(jogo.jogadores[0].jogadas)+1))
        
        for jogador in jogo.jogadores:
            atirou = False
            while not atirou:
                try:
                    jogador.atirar((random.randint(0,9), random.randint(0,9)))                    
                    atirou = True
                except:
                    continue
    
        print_jogo(jogo)

    
def print_jogo(jogo):
    chars = {
        Jogador.AGUA: '-',
        Jogador.TIRO_AGUA: '+',
        Jogador.EMBARCACAO: '#',
        Jogador.TIRO_EMBARCACAO: '@'
    }
    
    sep = "             "
    print("\n======================="+sep+"=======================")
    print(" ".join(['  ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']), end='', sep='')
    print(" ".join(['   '+sep, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']), end='', sep='')
    print("\n", end='')
    
    tabuleiros = []

    tabuleiros.append(jogo.jogadores[0].get_tabuleiro())
    tabuleiros.append(jogo.jogadores[1].get_tabuleiro())

    for y in xrange(0, 10):
        
        for tabuleiro in tabuleiros:
            print(" "+str(y+1) if (y+1) < 10 else y+1, end=" ", sep="")
            for x in xrange(0, 10):
                print(chars[tabuleiro[y][x]], end=" ", sep="")
                
            print(sep, end='', sep='')
            
        print("\n", end="", sep="")

    print("======================="+sep+"=======================\n")
            
if __name__ == "__main__":
    main()            
