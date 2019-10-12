# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:28:01 2019

@author: parju
"""

global n
n = 3

board = [[0 for i in range(n)] for j in range(n)]

# Step 3 - Validation
def isValid(board, row, col, n):
    # To validate in the rows
    if n in board[row]:
        return False
    # To validate in the columns
    for r in range(len(board)):
        if(board[r][col] == n):
            return False
    return True

# Step - Recursive Def
def SolveSquare(board, row, col):
    # Out Recursive Def
    if(row >= n):
        return True
    for num in range(1, n+1):
        if(isValid(board, row, col, num)):
            board[row][col] = num
            if(col == n-1):
                if(SolveSquare(board, row+1, 0)):
                    return True
            # Continue in the next col
            elif(SolveSquare(board, row, col+1)):
                return True
            board[row][col] = 0
    
    return False
    
def printBoard(board):
    if(SolveSquare(board, 0, 0)):
        for row in board:
            print(row)
    else:
        print("The solution doesn't exists")

printBoard(board)
