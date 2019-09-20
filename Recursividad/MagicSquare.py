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
    for num in board[row]:
        if(num == n):
            return False
    
    # To validate in the columns
    for r in range(len(board)):
        if(board[r][col] == n):
            return False
    
    return True

# Step - Recursive Def
def SolveSquare(board, row):
    # Out Recursive Def
    if(row >= n):
        return True
    
    # In the row iterate in each column and put the options
    for col in range(n):
        for num in range(1, n+1):
            if(isValid(board, row, col, num)):
                board[row][col] = num
                break
    
    # Continue in the next row
    if(SolveSquare(board, row+1)):
        return True

    return False
        
def printBoard(board):
    if(SolveSquare(board, 0)):
        for row in board:
            print(row)
    else:
        print("The solution doesn't exists")

printBoard(board)
