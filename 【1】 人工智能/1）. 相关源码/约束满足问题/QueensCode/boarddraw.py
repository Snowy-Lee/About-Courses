# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:29:34 2020

@author: duxiaoqin
Functions:
    (1)BoardDraw class;
    (2)If board'size is changed, then image's size is accordingly changed.
"""

from graphics import *
from board import *

class BoardDraw:
    def __init__(self, win, board, queenimg1, queenimg2):
        self.width = board.width
        self.height = board.height
        self.win = win
        self.win.setCoords(0.0, 0.0, self.width + 2, self.height + 2)
        
        self.rect_points = []
        for row in range(self.height):
            for col in range(self.width):
                point1 = Point(col+1, self.height-row)
                point2 = Point(col+1+1, self.height-row+1)
                if (row + col) % 2 == 0:
                    color = 'white'
                else:
                    color = 'gray'
                self.rect_points.append((point1, point2, color))
        self.rectangles = []
        for p1, p2, color in self.rect_points:
            rect = Rectangle(p1, p2)
            rect.setOutline('gray')
            rect.setFill(color)
            self.rectangles.append(rect)
            
        start, end = 1.0, self.height + 1
        
        self.queen1img = Image(Point(0, 0), queenimg1)
        self.queen1imgs = Array2D(self.height, self.width)
        self.queen2img = Image(Point(0, 0), queenimg2)
        self.queen2imgs = Array2D(self.height, self.width)
        for row in range(self.height):
            for col in range(self.width):
                newqueen1img = self.queen1img.clone()
                newqueen1img.move(start+1/2+col, end-1/2-row)
                self.queen1imgs[row, col] = newqueen1img
                
                newqueen2img = self.queen2img.clone()
                newqueen2img.move(start+1/2+col, end-1/2-row)
                self.queen2imgs[row, col] = newqueen2img
        
    def draw(self, board):
        for rect in self.rectangles:
            rect.undraw()
        for row in range(self.height):
            for col in range(self.width):
                self.queen1imgs[row, col].undraw()
                self.queen2imgs[row, col].undraw()
                
        for rect in self.rectangles:
            rect.draw(self.win)
        for row in range(self.height):
            for col in range(self.width):
                if board[row, col] == Board.OCCUPIED:
                    if (row + col) % 2 == 0:
                        self.queen1imgs[row, col].draw(self.win)
                    else:
                        self.queen2imgs[row, col].draw(self.win)
        update(30)
                
def main():
    win = GraphWin('BoardDraw', 600, 600, autoflush = False)
    board = Board(8)
    #board.board.clear(Board.OCCUPIED)
    board.print()
    #boarddraw = BoardDraw(win, board, 'Queen16-1.png', 'Queen16-2.png')
    boarddraw = BoardDraw(win, board, 'Queen8-1.png', 'Queen8-2.png')
    #boarddraw = BoardDraw(win, board, 'Queen4-1.png', 'Queen4-2.png')

    while win.checkKey() != 'Escape':
        boarddraw.draw(board)
    win.close()
    
if __name__ == '__main__':
    main()