# -*- coding: utf-8 -*-
"""
Backtracking
"""
n = 4


def imptablero(tablero):
	for i in range(n):
		for j in range(n):
			print(tablero[i][j], end=' ')
		print()


def asalvo(tablero, fila, columna):
	for i in range(columna):
		if(tablero[fila][i] == 1):
			return False

	for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):  # Diagonal izq, derecha
		if(tablero[i][j] == 1):
			return False

	for i, j in zip(range(fila, n, 1), range(columna, -1, -1)):  # diagonal derecha, izq
		if(tablero[i][j] == 1):
			return False

	return True


def solucion(tablero, columna):
	if(columna >= n):  # valida las columnas segun N
		return True

	for i in range(n):
		if(asalvo(tablero, i, columna)):
			tablero[i][columna] = 1

			if(solucion(tablero, columna + 1) is True):
				return True

			tablero[i][columna] = 0

	return False


def solucionNQ(): 
	tablero = [[0 for z in range(n)] for j in range(n)]

	if(solucion(tablero, 0) is False):
		print("Solution does not exist")
		return False

	imptablero(tablero)
	return True

# Driver Code


solucionNQ()
