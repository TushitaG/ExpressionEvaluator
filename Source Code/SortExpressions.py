
# Import modules
from Node import Node

# SortExpressions class sorts the expression based on their values, length and total number of brackets they have
class SortExpressions(Node): # All classes derive from class object
    def __init__(self, exp, value):
        self.exp = exp
        self.value = value
        self.brackets = exp.count('(' )+ exp.count(')')
        super().__init__() # Inherits its parent class Node
        
    # Overriding the inherited '==' function (from object class)
    def __eq__(self, otherNode):
        if otherNode == None:
            return False
        else:
            return self.exp==otherNode.exp  
    
    # Overriding the '<' operator (from object class)
    def __gt__(self, otherNode):
        if otherNode == None:
            raise TypeError("'>' not supported between instances of 'Temp' and 'NoneType'")
        return self.value>otherNode.value or (self.value==otherNode.value and len(self.exp)>len(otherNode.exp)) or (self.value==otherNode.value and len(self.exp)==len(otherNode.exp) and self.brackets>otherNode.brackets) 
    
    # Overriding the __str__ operator (from object class)
    def __str__(self):
        return f'{self.exp}={self.value}'