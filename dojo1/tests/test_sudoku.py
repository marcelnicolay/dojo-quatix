import unittest2
from sudoku.validate import SudokuValidator

class ValidateSudoku(unittest2.TestCase):
    
    def setUp(self):
        
        self.sudokuTabuleiro = SudokuTabuleiro()
    
    def test_is_invalid_game(self):
        
        tabuleiro = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
        
        self.assertTrue(self.sudokuValidator.validate())
        
    def test_is_invalid_line_number(self):
        line = [1,2,3,4,5,6,0,0,0]
        
        sudokuValidator = SudokuValidator([])

        with self.assertRaises(ValueError):
            sudokuValidator.getIndexErrorsInLine(line)
        
    def test_is_invalid_length_line(self):
        line = [1,2,3,4,5,6,7,8,9,9]
        
        sudokuValidator = SudokuValidator([])
        
        with self.assertRaises(ValueError):
            sudokuValidator.getIndexErrorsInLine(line)
        
    def test_is_invalid_length_matrix(self):
        
        matrix = [ 
            [1,2,3],
            [4,5,6,9],
            [7,8]
        ]
        
        sudokuValidator = SudokuValidator([])
        
        with self.assertRaises(ValueError):
            sudokuValidator.getIndexErrorInSubmatrix(matrix)
            
    def test_get_index_error_in_line(self):
        
        line = [1,2,2,3,4,4]
        
        sudokuValidator = SudokuValidator([])

        index_errors = sudokuValidator.getIndexErrorsInLine(line)
        self.assertEquals(index_errors, [1,2,4,5])

    def test_get_index_error_in_matrix(self):

        matrix = [
            [1,1],
            [2,3],
            [4,4,5]
        ]
        
        sudokuValidator = SudokuValidator([])
        
        index_errors = sudokuValidator.getIndexErrorInSubmatrix(matrix)
        self.assertEquals(index_errors, [(0,0),(0,1)])
        
