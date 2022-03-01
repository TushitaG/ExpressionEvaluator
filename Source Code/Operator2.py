
# Import modules
from Evaluate import Evaluate

# Subclass of Evaluate class
# Operator2 class to evaluate expressions based on operator 2 settings
class Operator2(Evaluate):
    def evaluate(self,tree):
        leftTree = tree.getLeftTree()
        rightTree = tree.getRightTree()
        op = tree.getKey()

        if leftTree != None and rightTree != None:
            if op == '+':
                return max(self.evaluate(leftTree),self.evaluate(rightTree))
            elif op == '-':
                return min(self.evaluate(leftTree),self.evaluate(rightTree))
            elif op == '*':
                return round(self.evaluate(leftTree) * self.evaluate(rightTree))
            elif op == '/':
                return round(self.evaluate(leftTree) / self.evaluate(rightTree))
            elif op == '**':
                return (self.evaluate(leftTree) % self.evaluate(rightTree))
        else:
            return tree.getKey()