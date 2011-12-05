class Jogador(object):
    
    AGUA = 0
    EMBARCACAO = 1
    TIRO_AGUA = 2
    TIRO_EMBARCACAO = 3
    
    def __init__(self):
        self.embarcacoes = []
        self.jogadas = []    

    def adicionar_embarcacao(self, embarcacao):
        for posicao_x, posicao_y in embarcacao.get_posicoes():
            if posicao_x > 9 or posicao_y > 9 or posicao_x < 0 or posicao_y < 0:
                raise ValueError() 

        for embarcacao_atual in self.embarcacoes:
            for posicao in embarcacao.get_posicoes():
                if posicao in embarcacao_atual.get_posicoes():
                    raise ValueError()
                    
        self.embarcacoes.append(embarcacao)

    def atirar(self, posicao):
        
        if posicao in self.jogadas:
            raise ValueError()
            
        self.jogadas.append(posicao)

        for embarcacao in self.embarcacoes:
            
            if posicao in embarcacao.get_posicoes():
                # Acertou a embarcacao
                
                for posicao_embarcacao in embarcacao.get_posicoes():
                    if posicao_embarcacao not in self.jogadas:
                        # ainda nao afundou
                        return embarcacao
                embarcacao.afundar()
                return embarcacao
        
        return None
        
    def get_tabuleiro(self):
        
        tabuleiro = []
        for y in range(0,10):
            tabuleiro.append([])
            for x in range(0,10):
                tabuleiro[y].append(Jogador.AGUA)
        
        for embarcacao in self.embarcacoes:
            for x, y in embarcacao.get_posicoes():
                tabuleiro[y][x] = Jogador.EMBARCACAO
                
        for x, y in self.jogadas:
            if tabuleiro[y][x] == Jogador.AGUA:
                tabuleiro[y][x] = Jogador.TIRO_AGUA
            else:
                tabuleiro[y][x] = Jogador.TIRO_EMBARCACAO
        
        return tabuleiro
        
    def is_terminado(self):
        
        for embarcacao in self.embarcacoes:
            if not embarcacao.afundado:
                return False
        
        return True