# coding: utf-8

class Carta(object):
    
    DOIS = 2
    TRES = 3
    QUATRO = 4
    CINCO = 5
    SEIS = 6
    SETE = 7
    OITO = 8
    NOVE = 9
    DEZ = 10
    VALETE = 11
    DAMA = 12
    REI = 13
    AS = 14
    
    OURO = 'D'
    COPAS = 'H'
    PAUS = 'C'
    ESPADAS = 'S'
    
    def __init__(self, valor, naipe):
        
        if valor not in (
            self.AS,
            self.DOIS,
            self.TRES,
            self.QUATRO,
            self.CINCO,
            self.SEIS,
            self.SETE,
            self.OITO,
            self.NOVE,
            self.DEZ,
            self.VALETE,
            self.DAMA,
            self.REI
        ):
            raise ValueError('valor da carta é invalido')
        
        if naipe not in (self.OURO, self.COPAS, self.PAUS, self.ESPADAS):
            raise ValueError('naipe da carta é invalido')
            
        self.valor = valor
        self.naipe = naipe
        
    def __repr__(self):
        return "%s%s" % (self.valor, self.naipe)