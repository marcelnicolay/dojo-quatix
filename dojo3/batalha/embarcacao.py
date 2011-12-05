class Embarcacao(object):
    
    def __init__(self, tamanho, posicao, is_horizontal):
        if tamanho > 5 or tamanho < 2:
            raise ValueError("Tamanho deve estar entre 2 e 5")
        self.tamanho = tamanho
        self.posicao = posicao
        self.is_horizontal = is_horizontal
        self.afundado = False
    
    def afundar(self):
        self.afundado = True

    def get_posicoes(self):
        posicoes = []
        
        for i in range(0, self.tamanho):
            if self.is_horizontal == True:
                posicao = (self.posicao[0]+i, self.posicao[1])
            else:
                posicao = (self.posicao[0], self.posicao[1]+i)
            posicoes.append(posicao)
            
        return posicoes

class PortaAvioes(Embarcacao):
    def __init__(self, *args, **kwargs):
        super(PortaAvioes, self).__init__(tamanho=5, *args, **kwargs)
        
class Encouracado(Embarcacao):
    def __init__(self, *args, **kwargs):
        super(Encouracado, self).__init__(tamanho=4, *args, **kwargs)
        
class Submarino(Embarcacao):
    def __init__(self, *args, **kwargs):
        super(Submarino, self).__init__(tamanho=3, *args, **kwargs)
        
class Destroyer(Embarcacao):
    def __init__(self, *args, **kwargs):
        super(Destroyer, self).__init__(tamanho=3, *args, **kwargs)
        
class Patrulha(Embarcacao):
    def __init__(self, *args, **kwargs):
        super(Patrulha, self).__init__(tamanho=2, *args, **kwargs)
                        
