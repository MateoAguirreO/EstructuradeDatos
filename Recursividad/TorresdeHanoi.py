# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:01:37 2019

@author: parju
"""

def hanoi(numero_discos, inicio=1, fin=3):
    if numero_discos:
        hanoi(numero_discos-1, inicio, 6-inicio-fin)
        print(f"Mueve el disco {numero_discos} de la torre {inicio} a la torre {fin}")
        hanoi(numero_discos-1, 6-inicio-fin, fin)
        
hanoi(3)