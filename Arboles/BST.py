# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:34:53 2019

@author: parju
"""

from Queue import Queue

class Node:
    def __init__(self, label, value, parent):
        self.label = label
        self.value = value
        self.parent = parent
        self.leftChild = None
        self.rightChild = None
        
    def hasLeftChild(self):
        if(self.leftChild):
            return True
        return False
    
    def hasRightChild(self):
        if(self.rightChild):
            return True
        return False


class BST:
    def __init__(self):
        self.root = None
        self.weight = 0
        self.depth = 1
        self.height = 0
    
    def getNodeLevel(self, node):
        if(node.parent == None):
            return 0
        
        return 1 + self.getNodeLevel(node.parent)
    
    def getHeight(self):
        return self.height
    
    def setHeight(self):
        self.height = self.depth - 1
    
    def getDepth(self):
        return self.depth
    
    def setDepth(self):
        nodes = self.preOrd()
        nodesLvl = []
        
        for node in nodes:
            nodesLvl.append(self.getNodeLevel(node))

        self.depth += max(nodesLvl)
    
    def getWeight(self):
        return self.weight
    
    def addNodes(self, list):
        for node in list:
            self.addNode(str(node), node)
        
        self.setDepth()
        self.setHeight()
    
    def addNode(self, label, value):
        if(self.root):
            self._addNode(label, value, self.root)
        else:
            self.root = Node(label, value, None)
        self.weight += 1
    
    def _addNode(self, label, value, parent):
        if(value > parent.value):
            if(parent.rightChild):
                self._addNode(label, value, parent.rightChild)
            else:
                parent.rightChild = Node(label, value, parent)
        elif(value < parent.value):
            if(parent.leftChild):
                self._addNode(label, value, parent.leftChild)
            else:
                parent.leftChild = Node(label, value, parent)
        else:
            print(f"Node {str(value)} already exists!")
    
    def pathWidth(self, node = None, queue = Queue()):
        if(not node):
            node = self.root
            queue.put(node)
               
        if(node.hasLeftChild()):
            queue.put(node.leftChild)        
        
        if(node.hasRightChild()):
            queue.put(node.rightChild)
        
        if(node.hasLeftChild()):
            self.pathWidth(node.leftChild, queue)
            
        if(node.hasRightChild()):
             self.pathWidth(node.rightChild, queue)
        return queue
    
    def _pathWidth(self, lvl = 0):
        if(lvl > self.getHeight()):
            return []
        
        unorderedNodeList = self.preOrd()
        orderedList = []
        
        for node in unorderedNodeList:
            if(self.getNodeLevel(node) == lvl):
                orderedList.append(node)
        
        return orderedList + self._pathWidth(lvl+1)
    
    def preOrd(self):
        if(self.root):
            nodeList = []
            nodeList = self._preOrd(self.root, nodeList)
            
            return nodeList
        else:
            print("Empty Tree")

    def _preOrd(self, node, preList):
        preList.append(node)
        
        if(node.hasLeftChild()):
            self._preOrd(node.leftChild, preList)
            
        if(node.hasRightChild()):
            self._preOrd(node.rightChild, preList)
        
        return preList
    
    def inOrd(self):
        if(self.root):
            nodeList = []
            nodeList = self._inOrd(self.root, nodeList)
            
            return nodeList
        else:
            print("Empty Tree")
    
    def _inOrd(self, node, inList):        
        if(node.leftChild):
            self._inOrd(node.leftChild, inList)
            
        inList.append(node)
        
        if(node.rightChild):
            self._inOrd(node.rightChild, inList)
        
        return inList
    
    def postOrd(self):
        if(self.root):
            nodeList =[]
            nodeList = self._postOrd(self.root, nodeList)
            
            return nodeList
        else:
            print("Empty Tree")
    
    def _postOrd(self, node, postList):
        if(node.leftChild):
            self._postOrd(node.leftChild, postList)   
            
        if(node.rightChild):
            self._postOrd(node.rightChild, postList) 
            
        postList.append(node)
        
        return postList
    
    def sumEvenmulOdd(self, lvl = 0):
        if(lvl > self.getHeight()):
            return None

        nodeList = self.preOrd()
        currentList = []
        result = 0
        
        for node in nodeList:
            if(self.getNodeLevel(node) == lvl):
                currentList.append(node.value)
        
        if(lvl%2 == 0):
            for num in currentList:
                result += num
        else:
            result = 1
            for num in currentList:
                result *= num
                
        print(result)
        
        self.sumEvenmulOdd(lvl+1)
    
    def externalNodes(self):
        allNodes = self.preOrd()
        currentList = []
        
        for node in allNodes:
            if(not node.hasLeftChild() and not node.hasRightChild()):
                print(node.value, end=',')
                currentList.append(node)
        
        return currentList
    
    def internalNodes(self):
        allNodes = self.preOrd()
        currentList = []
        
        for node in allNodes:
            if((node.hasLeftChild() or node.hasRightChild()) and node.parent):
                print(node.value, end=',')
                currentList.append(node)
        
        return currentList
                
        
            

l = (45,83,62,17,25,36,54,105,86,91,68,75,23,18,3)

myBST = BST()
myBST.addNodes(l)

myBST.internalNodes()

#pW = myBST.pathWidth()
#p = myBST.preOrd()
#
#print("Path in Pre-Order: ")
#for n in p:
#    if(p[-1] == n):
#        print(n.value)
#    else:
#        print(n.value, end=', ')
#
#print("Path in Width: ")
#for n in range(myBST.getWeight()):    
#    print(pW.get().value, end=', ')
    

