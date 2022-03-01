
# Import libraries and modules
from BinaryTree import BinaryTree
from VerticalTree import VerticalTree
from Stack import Stack
import re

# Parse tree function to solve the expression
class ParseTree:
    def __init__(self, exp, tree='tree1'):
        self.exp=exp
        self.tree=tree
        self.tokens=re.findall(r'[0-9\.]+|[0-9]+|[*+\/-]+[\*\*\s*]+|[^0-9]', exp.replace(' ',''))

    # Split each element in the expression and put into list
    def splitExp(self):
        tokens_cp = self.tokens.copy()
        score=0
        for i in range(len(self.tokens)):
            if ((tokens_cp[i]=='-') & (tokens_cp[i-1] in ['+', '-', '*', '/','**', '('])):
                if score>0:
                    del self.tokens[i-score]
                    if (self.tokens[i-score] not in ['+', '-', '*', '/','**', '(']):
                        self.tokens[i-score]='-'+self.tokens[i-score]
                        score=score+1
                else:
                    del self.tokens[i]
                    if (self.tokens[i] not in ['+', '-', '*', '/','**', '(']):
                        self.tokens[i]='-'+self.tokens[i]
                        score=score+1
        return self.tokens

    # Build the parse tree
    def buildParseTree(self):
        stack = Stack()

        ## Tree built according to print mode settings
        if self.tree=='tree1':
            tree = BinaryTree('?')
        elif self.tree=='tree2':
            tree = VerticalTree('?')

        stack.push(tree)
        currentTree = tree
        tokens=self.splitExp()

        for t in tokens:
            if t == '(':
                currentTree.insertLeft('?')
                stack.push(currentTree)
                currentTree = currentTree.getLeftTree()
           
            elif t in ['+', '-', '*', '/', '**']:
                currentTree.setKey(t)
                currentTree.insertRight('?')
                stack.push(currentTree)
                currentTree = currentTree.getRightTree()

            elif t not in ['+', '-', '*', '/','**', ')']:
                try:
                    currentTree.setKey(int(t))
                except ValueError:
                    currentTree.setKey(float(t))
                parent = stack.pop()
                currentTree = parent

            elif t == ')':
                currentTree = stack.pop()
            else:
                raise ValueError
        return tree

