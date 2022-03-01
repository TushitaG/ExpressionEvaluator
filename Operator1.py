# Name: Tushita Govindaraj
# StudentID: 
# Class: DAAA/FT/2B/02

# Import libraries and modules
from Evaluate import Evaluate
from ParseTree import ParseTree

# Subclass of Evaluate class
# Operator1 class to evaluate expressions based on operator 1 settings
class Operator1(Evaluate):
    def evaluate(self,tree):
        leftTree = tree.getLeftTree()
        rightTree = tree.getRightTree()
        op = tree.getKey()

        if leftTree != None and rightTree != None:
            if op == '+':
                return (self.evaluate(leftTree) + self.evaluate(rightTree))
            elif op == '-':
                return (self.evaluate(leftTree) - self.evaluate(rightTree))
            elif op == '*':
                return (self.evaluate(leftTree) * self.evaluate(rightTree))
            elif op == '/':
                return (self.evaluate(leftTree) / self.evaluate(rightTree))
            elif op == '**':
                return (self.evaluate(leftTree) ** self.evaluate(rightTree))
        else:
            return tree.getKey()