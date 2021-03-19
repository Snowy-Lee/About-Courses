# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 21:56:44 2020

@author: duxiaoqin
Functions:
    (1)Sudoku class;
"""

from myarray2d import Array2D

class Sudoku:
    EMPTY = 0
    def __init__(self, size):
        self.sudoku = Array2D(size, size)
        self.sudoku.clear(Sudoku.EMPTY)
        self.size = size
            
    def __getitem__(self, ndxTuple):
        return self.sudoku.__getitem__(ndxTuple)
    
    def __setitem__(self, ndxTuple, value):
        self.sudoku.__setitem__(ndxTuple, value)
        
    def print(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.sudoku[row, col] == Sudoku.EMPTY:
                    print('-', end=' ')
                else:
                    print(self.sudoku[row, col], end=' ')
            print()
            
def main():
    sudoku = Sudoku(9)
    sudoku.print()
    
if __name__ == '__main__':
    main()