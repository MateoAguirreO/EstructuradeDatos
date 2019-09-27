# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:03:02 2019

@author: parju
"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def put(self, item):
        self.items.insert(0,item)

    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)