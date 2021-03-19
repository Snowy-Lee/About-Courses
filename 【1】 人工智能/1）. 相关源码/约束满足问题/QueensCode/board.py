# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 14:57:53 2020

@author: duxiaoqin
Functions:
    (1)Board class
"""

from myarray2d import Array2D

class Board:
    EMPTY = 0
    OCCUPIED = 1
    def __init__(self, size):
        self.board = Array2D(size, size)
        self.board.clear(Board.EMPTY)
        self.height = size
        self.width = size
            
    def __getitem__(self, ndxTuple):
        return self.board.__getitem__(ndxTuple)
    
    def __setitem__(self, ndxTuple, value):
        self.board.__setitem__(ndxTuple, value)
        
    def print(self):
        for row in range(self.height):
            for col in range(self.width):
                if (row + col) % 2 == 0:
                    print('_', end=' ')
                else:
                    print('|', end=' ')
            print()
            
def main():
    board = Board(8)
    board.print()
    
if __name__ == '__main__':
    main()