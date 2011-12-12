from poker.carta import Carta

class Mao(object):
    
    def __init__(self, cartas):
        
        self.cartas = cartas
        self.ordenar_cartas()
        
    
    def is_royalflush(self):

        if not self.is_flush():
            return False
            
        if not self.is_straight():
            return False
            
        if self.cartas[0].valor != Carta.DEZ:
            return False
        
        return True
        
    def is_flush(self):
        naipe_default = self.cartas[0].naipe

        for carta in self.cartas:
            if carta.naipe != naipe_default:
                return False
                
        return True
        
    def is_four(self):
        conta_iguais = 0
        valores = [c.valor for c in self.cartas]
        carta_mais_comum = max(set(valores), key=valores.count)
        
        if valores.count(carta_mais_comum) == 4:
            return True
        
        return False
        
    def is_straight(self):
        
        cartas_ordenadas = [
            Carta.AS,
            Carta.DOIS,
            Carta.TRES,
            Carta.QUATRO,
            Carta.CINCO,
            Carta.SEIS,
            Carta.SETE,
            Carta.OITO,
            Carta.NOVE,
            Carta.DEZ,
            Carta.VALETE,
            Carta.DAMA,
            Carta.REI,
            Carta.AS
        ]

        indice_comeco = cartas_ordenadas.index(self.cartas[0].valor)
        
        for i in xrange(0, 5):
            if self.cartas[i].valor != cartas_ordenadas[i+indice_comeco]:
                return False
            
        return True
    
    def ordenar_cartas(self):
        
        self.cartas.sort(key=lambda c: c.valor)
        
        if  self.cartas[0].valor == Carta.DOIS and \
            self.cartas[1].valor == Carta.TRES and \
            self.cartas[2].valor == Carta.QUATRO and \
            self.cartas[3].valor == Carta.CINCO and \
            self.cartas[4].valor == Carta.AS:
        
            self.cartas.insert(0, self.cartas.pop())
            
        
            
            
    