

class SudokuValidator(object):
    
    def __init__(self, tabuleiro):
        
        self.tabuleiro = tabuleiro
        
        
    def validate(self):
        
        return True
    
    def getIndexErrorsInLine(self, line):

        if len(line) > 9:
            raise ValueError('itens demais na linha')
            
        index_errors = []
        
        for i in range(1, 10):
            if line.count(i) > 1:
                for index in range(0, len(line)):
                    if line[index] == i:
                        index_errors.append(index)
   
        for item in line:
            if item > 9 or item < 1:
                raise ValueError('intens invalidos na lista')
            
        return index_errors
        
    def getIndexErrorInSubmatrix(self, matrix):
        
        for linha in matrix:
            if len(linha) > 3:
                raise ValueError('Tamanho invalido da matriz')
                
        if len(matrix) > 3:
            raise ValueError('Tamanho invalido da matriz')

        

        all_numbers = []
        for line in matrix:
            numero_elementos = len(line)
            
            
            for number in line:
                all_numbers.append(number)

        index_errors = self.getIndexErrorsInLine(all_numbers)
        
        
        for index in index_errors:
            if index % 3