# -*- coding: utf-8 -*-
"""
Recursividad
"""

def Factorial(n):
    """
    Función que devuelve el factorial de un numero n.
    Se implementa usando Recursividad Lineal No Final.
    """
    
    if(n == 1):
        return n
    
    return n * Factorial(n-1)

def MCD(n, m):
    """
    Función que devuelve el Máximo Común Divisior entre dos numero n y m.
    Se implementa usando Recursividad Lineal Final.
    """
    
    if(n == m):
        return n
    elif(n > m):
        return MCD(n-m, m)
    elif(n < m):
        return MCD(n, m-n)

def Fib(n):
    """
    Función que devuelve el numero de Fibonacci correspondiente en la posición n.
    Se implementa usando Recursividad Múltiple.
    """
    
    if(n == 0 or n == 1):
        return n
    
    return Fib(n-1) + Fib(n-2)

n = 12
m = 18

print("Fibonacci en {}: {}".format(n, Fib(n)))
#print("MCD entre {} y {}: {}".format(n, m, MCD(n,m)))
#print("Factorial de ", Factorial(n))