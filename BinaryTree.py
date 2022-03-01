# Name: Tushita Govindaraj
# StudentID: 2012155
# Class: DAAA/FT/2B/02

# Binary class to build the expression tree
class BinaryTree:
    def __init__( self,key,leftTree = None, rightTree = None):
        self.key= key
        self.leftTree= leftTree
        self.rightTree= rightTree
        self.config='config.txt'
    
    # Stores an object in the root node
    def setKey (self, key):
        self.key= key
    
    # Returns object stored in root node
    def getKey (self):
        return self.key
    
    # Returns the Binary Tree stored as child at left hand site
    def getLeftTree (self):
        return self.leftTree
    
    # Returns the Binary Tree stored as child at right hand site
    def getRightTree (self):
        return self.rightTree
    
    # Creates new Binary Tree and insert it as child at left hand side
    def insertLeft(self,key):
        if self.leftTree == None:
            self.leftTree = BinaryTree(key)
        else:
            t = BinaryTree(key)
            self.leftTree, t.leftTree = t, self.leftTree
    
    # Creates a new Binary Tree and inserts it as child at right hand side
    def insertRight (self,key):
        if self.rightTree == None:
            self.rightTree = BinaryTree (key)
        else:
            t = BinaryTree (key)
            self.rightTree, t.rightTree = t, self.rightTree

    # read separator from config file
    def readSeparator(self):
        separator = open(self.config, "r").read().splitlines()[0]
        if separator not in ['.', '~', '|', '^', '#', '!', ':', '$', '<', '>', ' ']:
            separator='.'
        return separator
    
    # tree printed in preorder
    def printPreorder (self, level):
        separator = self.readSeparator()
        print(str(level*separator)+ str(self.key))
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1)

    # tree printed in inorder
    def printInorder(self, level):
        separator = self.readSeparator()
        if self.rightTree != None:
            self.rightTree.printInorder(level+1)
        print( str(level*separator) + str(self.key))
        if self.leftTree != None:
            self.leftTree.printInorder(level+1)