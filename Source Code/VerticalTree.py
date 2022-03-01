# Import modules
from BinaryTree import BinaryTree

# VerticalTree expression is similar to binary tree but this will print the expression tree vertically
class VerticalTree:
    def __init__( self,key,leftTree = None, rightTree = None):
        self.key= key
        self.leftTree= leftTree
        self.rightTree= rightTree
        self.output=''
    
    def setKey (self, key):
        self.key= key
    
    def getKey (self):
        return self.key
    
    def getLeftTree (self):
        return self.leftTree
    
    def getRightTree (self):
        return self.rightTree
    
    def insertLeft(self,key):
        if self.leftTree == None:
            self.leftTree = VerticalTree(key)
        else:
            t = VerticalTree(key)
            self.leftTree, t.leftTree = t, self.leftTree
    
    def insertRight (self,key):
        if self.rightTree == None:
            self.rightTree = VerticalTree (key)
        else:
            t = VerticalTree (key)
            self.rightTree, t.rightTree = t, self.rightTree

    def getSeparator(self):
        separator=BinaryTree('?').readSeparator()
        if separator=='.':
            separator='~'
        return separator
    
    # Print pre-order vertically
    def printPreorder(self, level):
        separator = self.getSeparator()
        self.output+=str(level*separator)+ str(self.key)+'\n'
        if self.leftTree != None:
            self.output+=self.leftTree.printPreorder(level+1)+'\n'
        if self.rightTree != None:
            self.output+=self.rightTree.printPreorder(level+1)+'\n'
        return self.output

    # Print in-order vertically
    def printInorder(self, level):
        separator = self.getSeparator()
        if self.rightTree != None:
            self.output += self.rightTree.printInorder(level+1)+'\n'
        self.output += str(level*separator) + str(self.key)+'\n'
        if self.leftTree != None:
            self.output+=self.leftTree.printInorder(level+1)+'\n'
        return self.output

    # Print the expression tree vertically
    def printAll(self, expList):
        result=''
        expList2=expList.copy()
        separator=self.getSeparator()
        for j in range(max([i.count(separator) for i in expList2])+1):
            result=''
            for k in range(len(expList)):
                try:
                    if expList[k][j].isdigit()==True or expList[k][j]=='-':
                        result+=expList[k][j:].ljust(len(expList[k][j]+ str(' '*(len(max(expList2, key=len))-max([i.count(separator) for i in expList])))), ' ')
                        expList[k]='d'
                    elif expList[k][j] in ['*','+','/','**',separator]:
                        result+=expList[k][j]+ str(' '*(len(max(expList2, key=len))-max([i.count(separator) for i in expList])))
                except:
                    result+=str(' '*(len(max(expList2, key=len))-max([i.count(separator) for i in expList])))+' '
            print(result)
    

