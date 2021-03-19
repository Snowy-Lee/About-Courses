# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 22:04:48 2020

@author: duxiaoqin
Functions:
    (1)SudokuDraw class;
"""

from graphics import *
from sudoku import *

class SudokuDraw:
    def __init__(self, win, sudoku):
        self.win = win
        self.sudoku = sudoku
        self.size = sudoku.size
        self.win.setCoords(0.0, 0.0, self.size + 2, self.size + 2)
        
        start, end = 1, self.size + 1
        for offset in range(sudoku.size + 1):
            l = Line(Point(start, start + offset), \
                     Point(end, start + offset))
            if offset % 3 == 0:
                l.setOutline('black')
                l.setWidth(3)
            else:
                l.setOutline('blue')
                l.setWidth(1)
            l.draw(self.win)
            l = Line(Point(start + offset, start), \
                     Point(start + offset, end))
            if offset % 3 == 0:
                l.setOutline('black')
                l.setWidth(3)
            else:
                l.setOutline('blue')
                l.setWidth(1)
            l.draw(self.win)
        
        self.stones = []
        for row in range(self.size):
            for col in range(self.size):
                if sudoku[row, col] != Sudoku.EMPTY:
                    text = Text(Point(start+1/2+col, end-1/2-row), sudoku[row, col])
                    text.setOutline('red')
                else:
                    text = Text(Point(start+1/2+col, end-1/2-row), '')
                    text.setOutline('black')
                text.setSize(12)
                text.draw(self.win)
                    
                self.stones.append(text)
        
    def draw_sudoku(self, sudoku):
        for row in range(self.size):
            for col in range(self.size):
                if sudoku[row, col] != Sudoku.EMPTY:
                    self.stones[row * self.size + col].setText(sudoku[row, col])                
                else:
                    self.stones[row * self.size + col].setText('')                
                    
    def draw(self, sudoku):
        self.draw_sudoku(sudoku)    
        self.win.update()
            
def main():
    win = GraphWin('Sudoku Draw', 600, 600, autoflush = False)
    sudoku = Sudoku(9)
    sudoku[0, 1], sudoku[0, 3], sudoku[0, 5], sudoku[0, 7] = 2, 5, 1, 9
    sudoku[1, 0], sudoku[1, 3], sudoku[1, 5], sudoku[1, 8] = 8, 2, 3, 6
    sudoku[2, 1], sudoku[2, 4], sudoku[2, 7] = 3, 6, 7
    sudoku[3, 2], sudoku[3, 6] = 1, 6
    sudoku[4, 0], sudoku[4, 1], sudoku[4, 7], sudoku[4, 8] = 5, 4, 1, 9
    sudoku[5, 2], sudoku[5, 6] = 2, 7
    sudoku[6, 1], sudoku[6, 4], sudoku[6, 7] = 9, 3, 8
    sudoku[7, 0], sudoku[7, 3], sudoku[7, 5], sudoku[7, 8] = 2, 8, 4, 7
    sudoku[8, 1], sudoku[8, 3], sudoku[8, 5], sudoku[8, 7] = 1, 9, 7, 6
    
    sudokudraw = SudokuDraw(win, sudoku)

    while win.checkKey() != 'Escape':
        sudokudraw.draw(sudoku)
    win.close()
    
if __name__ == '__main__':
    main()