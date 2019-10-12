# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:48:07 2019

@author: parju

N-QUEENS PROBLEM

Backtracking: 3-step to solving a problem with backtracking (brute force)

    1. Model the problem
    2. To define the main method (Recursive)
    3. Check the valid position or movement

Step 1: Model the problem
    Create a 0's matrix NxN
    global N = 4
    m = [[0 for i in range(N)] for j in range(N)]
    
Step 2: To define the main method (Recursive)
    def SolveProblem(board, col):
        if(col == N):
            return True
        
        for row in range(N):
            if(isValidPos(board, row, col)):
                board[row][col] = 1
                
                if(SolveProblem(board, col+1)):
                    return True
                board[row][col] = 0
    
Step 3: Check the valid position or movement
    def isValidPos(board, row, col):
        #Row  back
        for i in range(col, -1, -1):
            if(board[row][i] == 1):
                return False
        
        #Upper
        tuples = zip(range(row, -1, -1), range(col, -1, -1))
        
        for i,j in tuples:
            if(board[i,j] == 1):
                return False
        
        #Lower
        tuples = zip(range(row, N), range(col, -1, -1))
        
        for i,j in tuples:
            if(board[i][j] == 1):
                return False
        
        return False

In the end...
    def getSolution:
        if(SolveProblem(board, 0)):
            for L in board:
                print L
        else:
            print("The solution doesn't exists")
    
    getSolution()

"""

global N
N = 4

def SolveProblem(board, col):
    if(col == N):
        return True
    
    for row in range(N):
        if(isValidPos(board, row, col)):
            board[row][col] = 1
            
            if(SolveProblem(board, col+1)):
                return True
            board[row][col] = 0

def isValidPos(board, row, col):
    #Row  back
    for i in range(col, -1, -1):
        if(board[row][i] == 1):
            return False
    
    #Upper
    tuples = zip(range(row, -1, -1), range(col, -1, -1))
    
    for i,j in tuples:
        if(board[i][j] == 1):
            return False
    
    #Lower
    tuples = zip(range(row, N), range(col, -1, -1))
    
    for i,j in tuples:
        if(board[i][j] == 1):
            return False
    
    return False
    
def getSolution(board):
    if(SolveProblem(board, 0)):
         for L in board:
             print(L)
    else:
        print("The solution doesn't exists!")
        

board = [[0 for i in range(N)] for j in range(N)]

getSolution(board)
