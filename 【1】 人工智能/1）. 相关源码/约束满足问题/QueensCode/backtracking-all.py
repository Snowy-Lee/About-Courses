# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 11:42:47 2020

@author: duxiaoqin
Functions:
    (1)Backtracking Algorithm for all solutions;
"""

import copy
from time import *
from graphics import *
from board import *
from boarddraw import *

def Consistent(Xi, vi, Solution):
    for Xj, vj in Solution:
        if Xi == Xj or vi == vj or abs(Xi - Xj) == abs(vi - vj):
            return False
    return True

def Backtracking(Vars, Solution, Solutions):
    Xi, Vi = Vars[0]
    for vi in Vi:
        if Consistent(Xi, vi, Solution):
            Solution.append((Xi, vi))
            if len(Vars) == 1:
                Solutions.append(copy.deepcopy(Solution))
            else:
                VarsC = copy.deepcopy(Vars)
                VarsC.pop(0)
                Backtracking(VarsC, Solution, Solutions)
            Solution.pop()

def main():
    win = GraphWin('Backtracking', 600, 600, autoflush = False)
    board = Board(8)

    Vars = []
    for row in range(board.height):
        Vars.append((row, list(range(board.width))))
    Solutions = []
    Solution = []
    Backtracking(Vars, Solution, Solutions)
    
    boarddraw = BoardDraw(win, board, 'Queen8-1.png', 'Queen8-2.png')

    text = Text(Point(board.width/2+1, 0.5), '')
    text.setTextColor('red')
    text.draw(win)

    for index, Solution in enumerate(Solutions):
        text.setText('{}/{} Solutions'.format(index+1, len(Solutions)))
        board.board.clear(Board.EMPTY)
        for Xi, vi in Solution:
            board[Xi, vi] = Board.OCCUPIED
        boarddraw.draw(board)
        time.sleep(0.25)
        if win.checkKey() == 'Escape':
            win.close()
            exit()
    time.sleep(1.0)
    win.close()
    
if __name__ == '__main__':
    main()