from BST import Node

class AVL:
    def __init__(self):
        self.root = None
    
    def getNodeDepth(self, node):        
        if(node):
            if(node.isLeaf()):
                return 1
            
            lw = self.getNodeDepth(node.getLeftChild())
            rw = self.getNodeDepth(node.getRightChild())
            
            return (max(lw, rw) + 1)
        else:
            return 0
    
    def getBalanceFactor(self, node):
        if(not node):
            return 0
        
        if(node.isLeaf()):
            return 0
        
        leftD, rightD = 0, 0
        
        leftD = self.getNodeDepth(node.getLeftChild())
        rightD = self.getNodeDepth(node.getRightChild())
        
        return leftD - rightD
    
    def verifyBalance(self, node):
        bF = self.getBalanceFactor(node)
        
        if(bF >= -1 and bF <= 1):
            if(not node.isRoot()):
                self.verifyBalance(node.getParent())
        else:
            if(bF > 0):
                leftC = node.getLeftChild()
                leftCbF = self.getBalanceFactor(leftC)
                
                if(leftCbF > 0):
                    self.turnLL(leftC, leftC.getLeftChild())
                else:
                    self.turnLR(leftC, leftC.getRightChild())
            else:
                rightC = node.getRightChild()
                rightCbF = self.getBalanceFactor(rightC)
                
                if(rightCbF > 0):
                    self.turnRL(rightC, rightC.getLeftChild())
                else:
                    self.turnRR(rightC, rightC.getRightChild())
    
    def turnLL(self, pivot, grandSon):
        grandPa = pivot.getParent()
        grandSon.setParent(grandPa)
        
        if(pivot.isLeftChild):
            grandPa.setLeftChild(grandSon)
        else:
            grandPa.setRightChild(grandSon)
        
        pivot.setParent(grandSon)
        
        if(grandSon.hasRightChild()):
            pivot.setLeftChild(grandSon.getRightChild())
            grandSon.getRightChild().setParent(pivot)
        
        grandSon.setRightChild(pivot)
    
    def turnLR(self, pivot, grandSon):
        self.turnLL(grandSon, grandSon.getRightChild())
        self.turnRR(pivot, pivot.getLeftChild())
    
    def turnRR(self, pivot, grandSon):
        grandPa = pivot.getParent()
        grandSon.setParent(grandPa)
        
        if(pivot.isLeftChild):
            grandPa.setLeftChild(grandSon)
        else:
            grandPa.setRightChild(grandSon)
        
        pivot.setParent(grandSon)
        
        if(grandSon.hasLeftChild()):
            pivot.setRightChild(grandSon.getLeftChild())
            grandSon.getLeftChild().setParent(pivot)
        
        grandSon.setLeftChild(pivot)
    
    def turnRL(self, pivot, grandSon):
        self.turnRR(grandSon, grandSon.getLeftChild())
        self.turnLL(pivot, pivot.getRightChild())
            
    
    def addNodes(self, list):
        for node in list:
            self.addNode(str(node), node)

    def addNode(self, label, value):
        if(self.root):
            self._addNode(label, value, self.root)
        else:
            self.root = Node(label, value, None)

    def _addNode(self, label, value, parent):
        newNode = Node(label, value, parent)
        
        if(value > parent.value):
            if(parent.rightChild):
                self._addNode(label, value, parent.rightChild)
            else:
                parent.setRightChild(newNode)
        elif(value < parent.value):
            if(parent.leftChild):
                self._addNode(label, value, parent.leftChild)
            else:
                parent.setLeftChild(newNode)
        else:
            print(f"Node {str(value)} already exists!")
        
        if(not newNode.isRoot() and not newNode.getParent().isRoot() and not newNode.getGrandPa().isRoot()):
            self.verifyBalance(newNode.getGrandPa())
    
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


listofNodes = [54, 26, 8, 77, 63, 35, 43, 69, 59, 56, 55, 58, 86, 79, 100]

myAVL = AVL()
myAVL.addNodes(listofNodes)
l = myAVL.preOrd()

for node in l:
    print(node.value, end=', ')
    
print("")

    