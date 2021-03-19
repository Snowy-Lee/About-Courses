# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:57:06 2020

@author: duxiaoqin
Functions:
    (1)Backtracking Algorithm for all solutions;
"""

import copy
from time import *
from graphics import *
from sudoku import *
from sudokudraw import *

def SameBlock(row_i, col_i, row_j, col_j):
    if abs(row_i - row_j) >= 3 or abs(col_i - col_j) >= 3:
        return False
    if ((0 <= row_i <= 2 and 0 <= row_j <= 2) or \
        (3 <= row_i <= 5 and 3 <= row_j <= 5) or \
        (6 <= row_i <= 8 and 6 <= row_j <= 8)) and \
       ((0 <= col_i <= 2 and 0 <= col_j <= 2) or \
        (3 <= col_i <= 5 and 3 <= col_j <= 5) or \
        (6 <= col_i <= 8 and 6 <= col_j <= 8)):
           return True
    else:
        return False

def Consistent(rowcol_i, vi, Solution):
    row_i, col_i = rowcol_i
    for (row_j, col_j), vj in Solution:
        if (row_i == row_j or col_i == col_j or SameBlock(row_i, col_i, row_j, col_j)) and vi == vj:
            return False
    return True

def Backtracking(Vars, Solution, Solutions):
    (row, col), Vi = Vars[0]
    for vi in Vi:
        if Consistent((row, col), vi, Solution):
            Solution.append(((row, col), vi))
            if len(Vars) == 1:
                Solutions.append(copy.deepcopy(Solution))
            else:
                VarsC = copy.deepcopy(Vars)
                VarsC.pop(0)
                Backtracking(VarsC, Solution, Solutions)
            Solution.pop()

def main():
    win = GraphWin('Backtracking', 600, 600, autoflush = False)
    sudoku = Sudoku(9)
    sudoku[0, 1], sudoku[0, 5], sudoku[0, 7] = 2, 1, 9
    sudoku[1, 0], sudoku[1, 3], sudoku[1, 8] = 8, 2, 6
    sudoku[2, 1], sudoku[2, 4], sudoku[2, 7] = 3, 6, 7
    sudoku[3, 2], sudoku[3, 6] = 1, 6
    sudoku[4, 0], sudoku[4, 1], sudoku[4, 7], sudoku[4, 8] = 5, 4, 1, 9
    sudoku[5, 2], sudoku[5, 6] = 2, 7
    sudoku[6, 1], sudoku[6, 4], sudoku[6, 7] = 9, 3, 8
    sudoku[7, 0], sudoku[7, 3], sudoku[7, 5], sudoku[7, 8] = 2, 8, 4, 7
    sudoku[8, 1], sudoku[8, 3], sudoku[8, 5], sudoku[8, 7] = 1, 9, 7, 6

    sudokudraw = SudokuDraw(win, sudoku)
    text = Text(Point(sudoku.size/2+1, 0.5), 'Searching...')
    text.setTextColor('red')
    text.draw(win)
    sudokudraw.draw(sudoku)
    
    Vars = []
    Solution = []
    for row in range(sudoku.size):
        for col in range(sudoku.size):
            if sudoku[row, col] != Sudoku.EMPTY:
                Solution.append(((row, col), sudoku[row, col]))
            else:
                Vars.append(((row, col), list(range(1, sudoku.size + 1))))
    Solutions = []
    Backtracking(Vars, Solution, Solutions)

    for index, Solution in enumerate(Solutions):
        text.setText('{}/{} Solutions'.format(index+1, len(Solutions)))
        for (row, col), value in Solution:
            sudoku[row, col] = value
        sudokudraw.draw(sudoku)
        time.sleep(1.0)
        if win.checkKey() == 'Escape':
            win.close()
            exit()
    win.getKey()
    win.close()    
   
if __name__ == '__main__':
    main()