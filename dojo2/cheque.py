#coding: utf-8

from decimal import Decimal

class Cheque(object):

    unidades = {1:'um', 2:'dois', 3:'três', 4: 'quatro', 5: 'cinco', 6 : 'seis', 7: 'sete', 8:'oito', 9: 'nove'}
    dezenas = {10: 'dez',11: 'onze',12: 'doze',13: 'treze',14: 'quatorze',15: 'quinze',16: 'dezesseis',17: 'dezessete',18: 'dezoito',19: 'dezenove',20: 'vinte',30: 'trinta',40: 'quarenta',50: 'cinquenta',60: 'sessenta',70: 'setenta',80: 'oitenta',90: 'noventa'}
    centenas = {
        100: 'cem',
        200: 'duzentos',
        300: 'trezentos',
        400: 'quatrocentos',
        500: 'quinhentos',
        600: 'seiscentos',
        700: 'setecentos',
        800: 'oitocentos',
        900: 'novecentos',
    }
    
    def __init__(self, valor):
        
        if valor <= 0:
            raise ValueError('Número inválido')
            
        self.valor = Decimal(str(valor))

    def get_unidade(self, unidade):
        return Cheque.unidades[unidade]
        
    def get_dezena(self, dezena):
        if dezena < 10:
            return self.get_unidade(dezena)

        if dezena < 20 or dezena % 10 == 0:
            return Cheque.dezenas[dezena]
        else:
            unidade = dezena % 10
            grandeza = dezena - unidade
            return "%s e %s" % (Cheque.dezenas[grandeza], self.get_unidade(unidade))

    def get_centena(self, centena):
        
        if centena < 100:  
            return self.get_dezena(centena)
        
        if centena > 100 and centena < 200:
            return 'cento e ' + self.get_dezena(centena-100)
        else:
            if centena % 100 == 0:
                return Cheque.centenas[centena]
            else:
                dezena = centena % 100
                grandeza = centena - dezena
                return "%s e %s" % (Cheque.centenas[grandeza], self.get_dezena(dezena))
    
    def get_milhar_por_extenso(self, milhar):
        if milhar < 1000:
            return self.get_centena(milhar)
            
        grandeza = int(milhar/1000)

        if milhar % 1000 == 0:
            return "%s mil" % self.get_centena(grandeza)
        else:
            centena = milhar % 1000
            if centena < 100:
                return "%s mil e %s" % (self.get_centena(grandeza),self.get_centena(centena))
            else:
                return "%s mil %s" % (self.get_centena(grandeza),self.get_centena(centena))

    def get_valor_por_extenso(self):
        valor_centavos = (self.valor - int(self.valor)) * 100

        if int(self.valor) > 0:
            valor_por_extenso = str(self.get_milhar_por_extenso(int(self.valor)))
            valor_por_extenso+= " reais" if self.valor > 1 else " real"
            if valor_centavos > 0:
                valor_por_extenso += " e "
        else:
            valor_por_extenso = ""

        if valor_centavos > 0:
            valor_por_extenso += str(self.get_dezena(int(valor_centavos)))
            valor_por_extenso += " centavos" if valor_centavos > 1 else " centavo"
        
        return valor_por_extenso