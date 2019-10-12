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

def BinDec(n):
    """
    Función que convierte el # n en base 2 a numero en base 10.
    Se implementa usando Recursividad Lineal No Final.
    """
    
    s = str(n)
    if(len(s) == 1):
        return n
    mult = pow(2, (len(s)-1)) * int(s[0])
    
    return mult + BinDec(int(s[1:len(s)]))

def DecBin(n):
    """
    Función que convierte el # n en base 10 a numero en base 2.
    Se implementa usando Recursividad Lineal No Final.
    """
    
    if(n < 2):
        return n
    
    return n%2 + (10 * DecBin(n//2))

m = 110101
n = 53

#print("Fibonacci en {}: {}".format(n, Fib(n)))
#print("MCD entre {} y {}: {}".format(n, m, MCD(n,m)))
#print("Factorial de ", Factorial(n))
print("Decimal: ", n, " a Binario es: ", DecBin(n))