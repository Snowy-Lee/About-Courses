# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 11:00:23 2020

@author: duxiaoqin
Functions:
    (1)Backtracking Algorithm for one solution;
"""

from graphics import *
from board import *
from boarddraw import *
import copy

def Consistent(Xi, vi, Solution):
    for Xj, vj in Solution:
        if Xi == Xj or vi == vj or abs(Xi - Xj) == abs(vi - vj):
            return False
    return True

def Backtracking(Vars, Solution):
    Xi, Vi = Vars[0]
    for vi in Vi:
        if Consistent(Xi, vi, Solution):
            Solution.append((Xi, vi))
            if len(Vars) == 1:
                return True
            else:
                VarsC = copy.deepcopy(Vars)
                VarsC.pop(0)
                if Backtracking(VarsC, Solution):
                    return True
                else:
                    Solution.pop()
    return False

def main():
    win = GraphWin('Backtracking', 600, 600, autoflush = False)
    board = Board(8)

    Vars = []
    for row in range(board.height):
        Vars.append((row, list(range(board.width))))
    Solution = []
    Backtracking(Vars, Solution)
    
    for Xi, vi in Solution:
        board[Xi, vi] = Board.OCCUPIED

    boarddraw = BoardDraw(win, board, 'Queen8-1.png', 'Queen8-2.png')

    while win.checkKey() != 'Escape':
        boarddraw.draw(board)
    win.close()
    
if __name__ == '__main__':
    main()