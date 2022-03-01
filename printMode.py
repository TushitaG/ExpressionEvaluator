# Name: Tushita Govindaraj
# StudentID: 2012155
# Class: DAAA/FT/2B/02
# Data structure to store a binary tree node
from Node import Node
from BST import BST
from queue import Queue
# Vertical Class to print vertical sum, diagonal sum, sum of nodes
class Vertical:
    def __init__(self, root):
        self.root = root
    #SUms the vertical nodes of Binary Tree
    def VerticalSum(self,root,dist, dictionary):
        if not root:
            return
        dictionary[dist] = dictionary.get(dist, 0) + root.key
        self.VerticalSum(root.leftTree, dist - 1, dictionary)
        self.VerticalSum(root.rightTree, dist + 1, dictionary)
    #Prints the sum of Vertical nodes of Binary Tree
    def printVerticalSum(self):
        d = {}
        s = 1
        self.VerticalSum(self.root, 0, d)
        for key in sorted(d.keys()):
            print( f'Sums of node in Vertical {s} is: {d.get(key)}')
            s+=1
    #Counts number of levels a binary Tree has
    def getlevelofTree(self, root):
        if (root.leftTree == None and root.rightTree == None):
            return 0
 
        left = 0
        if (root.leftTree != None):
            left = self.getlevelofTree(root.leftTree)
    
        right = 0
        if (root.rightTree != None):
            right = self.getlevelofTree(root.rightTree)
    
        return (max(left, right) + 1)
    # Counts total sum of Nodes in a Binary Tree
    def totalSum(self,root):
        if root is None:
            return 0
        Q = Queue()
        Q.put(root)
        current_sum = 0
        while not Q.empty():
            node = Q.get()
            if node is None:
                continue
            current_sum = current_sum + node.key
            Q.put(node.leftTree)
            Q.put(node.rightTree)
        return current_sum
    # Finds the diagonal nodes of a Binary Tree
    def diagonalSumUtil(self,root, vd, diagonalSum) :
    
        if(not root):
            return
            
        if vd not in diagonalSum:
            diagonalSum[vd] = 0
        diagonalSum[vd] += root.key
        self.diagonalSumUtil(root.leftTree, vd + 1,
                            diagonalSum)
        self.diagonalSumUtil(root.rightTree, vd,
                        diagonalSum)
    #Sums the diagonal nodes in the Binary Tree
    def diagonalSum(self, root) :
        diagonalSum = dict()
        
        self.diagonalSumUtil(root, 0, diagonalSum)
        
        for sum in diagonalSum:
            print(f'Sum of Diagonal {sum+1} is: {diagonalSum[sum]}')



    