# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 19:58:46 2019

@author: parju
"""

l = ["a", 2, 3, "d"]

def invertir(list, last):
    if(list.index(last) == 0):
        return True
    
    n = list[0]
    list.insert(list.index(last)+1, n)
    list.pop(0)
    
    return invertir(list, last)

def invertir2(list):
    if len(list) == 0:
        return []
    
    return [list[-1]] + invertir2(list[:-1])

#invertir(l, l[-1])

print(invertir2(l))