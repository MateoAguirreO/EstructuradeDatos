from BST import Node

class AVL:
    def __init__(self):
        self.root = None
    
    def getNodeLevel(self, nodeP, nodeC):
        if(nodeC.getParent() == nodeP):
            return 1

        return 1 + self.getNodeLevel(nodeP, nodeC.getParent())
    
    def getNodeDepth(self, nodeP, list=[]):
        nodes = self._preOrd(nodeP, [])
        nodes.pop(0)
        
        if(not nodes):
            return 0
        
        for node in nodes:
            list.append(self.getNodeLevel(nodeP, node))
        
        return max(list)
    
    def addNodes(self, list):
        for node in list:
            self.addNode(str(node), node)

    def addNode(self, label, value):
        if(self.root):
            self._addNode(label, value, self.root)
        else:
            self.root = Node(label, value, None)

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

print(myAVL)
    