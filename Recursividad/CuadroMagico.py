# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:58:37 2019

@author: parju
"""

global n
n = 3

board = [[0 for i in range(n)] for j in range(n)]

def SolveProblem(board, row, col):
    if(row >= 3):
        return True
    
    for n in range(1,4):
        if(isValidNumber(board, row, col, n)):
            board[row][col] = n
            return True
        if(col >= 2):
           if(SolveProblem(board, row+1, 0)):
               return True
        
        board[row][col] = 0
        
def isValidNumber(board, row, col, n):
    for num in board[row]:
        if(num == n):
            return False
    
    for i in range(3):
        if(board[i][col] == n):
            return False
    
    return True

SolveProblem(board, 0, 0)

for row in board:
    print(row)
